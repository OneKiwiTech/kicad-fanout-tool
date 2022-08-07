from ..model.model import Model
from ..view.view import FanoutView
from .logtext import LogText
import sys
import logging
import logging.config
import wx
import pcbnew
import math

class Controller:
    def __init__(self, board):
        self.view = FanoutView()
        self.board = board
        self.reference = None
        self.tracks = []
        self.vias = []
        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(self.board, self.logger)

        # Connect Events
        self.view.buttonFanout.Bind(wx.EVT_BUTTON, self.OnButtonFanout)
        
        self.add_references()
        self.get_tracks_vias()

    def Show(self):
        self.view.Show()
    
    def Close(self):
        self.view.Destroy()

    def OnButtonFanout(self, event):
        reference = self.view.GetReferenceSelected()
        if reference == '':
            self.logger.error('Please chose a Reference')
            return
        else:
            self.logger.info('Selected reference: %s' %reference)
            
        if len(self.tracks) > 0:
            track_index = self.view.GetTrackSelectedIndex()
        else:
            self.logger.error('Please add track width')
            return
        if len(self.tracks) > 0:
            via_index = self.view.GetViaSelectedIndex()
        else:
            self.logger.error('Please add via')
            return
        self.model.update_data(reference, self.tracks[track_index], self.vias[via_index])

    def add_references(self):
        references = []
        footprints = self.board.GetFootprints()
        for footprint in footprints:
            ref = str(footprint.GetReference())
            references.append(ref)
        self.view.AddReferences(references)

    def get_tracks_vias(self):
        units = pcbnew.GetUserUnits()
        unit = ''
        scale = 1
        # pcbnew.EDA_UNITS_INCHES = 0
        if units == pcbnew.EDA_UNITS_INCHES:
            unit = 'in'
            scale = 25400000
        # pcbnew.EDA_UNITS_MILLIMETRES = 1
        elif units == pcbnew.EDA_UNITS_MILLIMETRES:
            unit = 'mm'
            scale = 1000000
        # pcbnew.EDA_UNITS_MILS = 5
        elif units == pcbnew.EDA_UNITS_MILS:
            unit = 'mil'
            scale = 25400
        else:
            unit = 'mil'
            scale = 25400
        tracks = self.board.GetDesignSettings().m_TrackWidthList
        vias = self.board.GetDesignSettings().m_ViasDimensionsList
        tracklist = []
        vialist = []
        for track in tracks:
            if track > 0:
                self.tracks.append(track)
                display = str(track/scale) + ' ' + unit
                tracklist.append(display)
        # pcbnew.VIA_DIMENSION
        for via in vias:
            if via.m_Diameter > 0:
                self.vias.append(via)
                diam = via.m_Diameter
                hole = via.m_Drill
                display = str(diam/scale) + ' / ' + str(hole/scale) + ' ' + unit
                vialist.append(display)
        self.view.AddTracksWidth(tracklist)
        self.view.AddViasSize(vialist)
        self.logger.info('get_design_settings')

    def init_logger(self, texlog):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        # Log to stderr
        handler1 = logging.StreamHandler(sys.stderr)
        handler1.setLevel(logging.DEBUG)
        # and to our GUI
        handler2 = LogText(texlog)
        handler2.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(funcName)s -  %(message)s",
            datefmt="%Y.%m.%d %H:%M:%S",
        )
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)
        root.addHandler(handler1)
        root.addHandler(handler2)
        return logging.getLogger(__name__)
    