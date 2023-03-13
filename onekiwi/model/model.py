import pcbnew
from ..kicad.board import get_current_unit
from .bga import BGA

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.unit = get_current_unit()
        self.board = board
        self.references = []
        self.reference = None
        self.track = None
        self.via = None
        self.package = None
        self.alignment = None
        self.direction = None
        self.update_reference()

    def update_reference(self):
        footprints = self.board.GetFootprints()
        for footprint in footprints:
            ref = str(footprint.GetReference())
            self.references.append(ref)

    def update_data(self, reference, track, via):
        self.reference = reference
        self.track = track
        self.via = via

    def update_package(self, package, alignment, direction):
        self.package = package
        self.alignment = alignment
        self.direction = direction

    def fanout(self):
        if self.package == 'BGA':
            self.bga = BGA(
                self.board, self.reference, self.track, self.via, 
                self.alignment, self.direction, self.logger
            )
            self.bga.fanout()
    
    def remove_track_via(self):
        self.bga.remove_track_via()

    
