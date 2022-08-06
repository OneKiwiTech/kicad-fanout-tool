import pcbnew
from ..kicad.board import get_current_unit
from .bga import BGA

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.unit = get_current_unit()
        self.board = board
        self.reference = None
        self.track = None
        self.via = None

    def update_data(self, reference, track, via):
        self.reference = reference
        self.track = track
        self.via = via
        self.bga = BGA(self.board, self.reference, self.track, self.via, self.logger)

    
