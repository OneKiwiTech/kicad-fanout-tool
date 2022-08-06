import pcbnew
from ..kicad.board import get_current_unit

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.unit = get_current_unit()
        self.reference = None
        self.board = board
    
    def update_reference(self, reference):
        self.reference = reference

    
