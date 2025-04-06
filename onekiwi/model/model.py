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
        self.skip = 0
        self.track = None
        self.via = None
        self.unused_pads=None
        self.package = None
        self.alignment = None
        self.direction = None
        self.indexSelected = None
        self.update_reference()


    def update_reference(self):
        footprints = self.board.GetFootprints()
        for index,footprint in enumerate(footprints):
            if footprint.IsSelected():
                self.indexSelected = index
            ref = str(footprint.GetReference())
            self.references.append(ref)

    def update_data(self, reference,skip, track, via, unused_pads):
        self.reference = reference
        self.skip = skip
        self.track = track
        self.via = via
        self.unused_pads = unused_pads

    def update_package(self, package, alignment, direction):
        self.package = package
        self.alignment = alignment
        self.direction = direction

    def fanout(self):
        if self.package == 'BGA':
            self.bga = BGA(
                self.board, self.reference,self.skip, self.track, self.via, self.unused_pads, 
                self.alignment, self.direction, self.logger
            )
            self.bga.fanout()
    
    def remove_track_via(self):
        self.bga.remove_track_via()

    
