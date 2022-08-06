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
        self.model = Model(pcbnew.GetBoard(), self.logger)

        # Connect Events
        self.view.buttonFanout.Bind(wx.EVT_BUTTON, self.OnButtonFanout)
        #pcbnew.GetBoard()
        
        self.add_references()
        self.get_tracks_vias()
        self.footprint = self.board.FindFootprintByReference('U3')
        self.angle = self.footprint.GetOrientationDegrees()
        self.pads = self.footprint.Pads()
        self.x0 = self.footprint.GetPosition().x
        self.y0 = self.footprint.GetPosition().y
        self.radian = self.footprint.GetOrientationRadians()
        self.degrees = self.footprint.GetOrientationDegrees()

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
        """
        self.logger.info('Update %s' %self.angle)
        minx = self.pads[0].GetPosition().x
        maxx = self.pads[0].GetPosition().x
        miny = self.pads[0].GetPosition().y
        maxy = self.pads[0].GetPosition().y
        if self.degrees not in [0.0 , 90.0, 180.0, -90.0]:
            self.footprint.SetOrientationDegrees(0)
        for ind, pad in enumerate(self.pads, 1):
            if minx > pad.GetPosition().x:
                minx = pad.GetPosition().x
            if maxx < pad.GetPosition().x:
                maxx = pad.GetPosition().x
            if miny > pad.GetPosition().y:
                miny = pad.GetPosition().y
            if maxy < pad.GetPosition().y:
                maxy = pad.GetPosition().y
        self.footprint.SetOrientationDegrees(self.degrees)
        self.logger.info('min: %d, %d' %(minx, miny))
        self.logger.info('max: %d, %d' %(maxx, maxy))

        if self.degrees in [0.0 , 90.0, 180.0, -90]:
            x = (minx + maxx)/2
            y = (miny + maxy)/2
            start1 = pcbnew.wxPoint(x, maxy)
            end1 = pcbnew.wxPoint(x, miny)
            start2 = pcbnew.wxPoint(minx, y)
            end2 = pcbnew.wxPoint(maxx, y)
            track1 = pcbnew.PCB_TRACK(self.board)
            track1.SetStart(start1)
            track1.SetEnd(end1)
            track1.SetLayer(pcbnew.F_Cu)
            self.board.Add(track1)

            track2 = pcbnew.PCB_TRACK(self.board)
            track2.SetStart(start2)
            track2.SetEnd(end2)
            track2.SetLayer(pcbnew.F_Cu)
            self.board.Add(track2)
        else:
            anphal = math.tan(self.radian)
            self.logger.info('x0: %d, y0: %d' %(self.x0, self.y0))
            b1 = self.y0 + anphal*self.x0
            x1 = minx
            x2 = maxx

            y3 = (-1)*anphal*x1 + b1
            y4 = (-1)*anphal*x2 + b1
            start2 = pcbnew.wxPoint(x1, y3)
            end2 = pcbnew.wxPoint(x2, y4)
            self.logger.info('start2: %d, %d' %(x1, y3))
            self.logger.info('end2: %d, %d' %(x2, y4))

            track2 = pcbnew.PCB_TRACK(self.board)
            track2.SetStart(start2)
            track2.SetEnd(end2)
            track2.SetLayer(pcbnew.F_Cu)
            self.board.Add(track2)

            ax = 1/anphal
            bx = self.y0 - ax*self.x0

            y1 = ax*x1 + bx
            y2 = ax*x2 + bx
            self.logger.info('anphal: %f, b0: %f' %(anphal, bx))
            start3 = pcbnew.wxPoint(x1, y1)
            end3 = pcbnew.wxPoint(x2, y2)

            track3 = pcbnew.PCB_TRACK(self.board)
            track3.SetStart(start3)
            track3.SetEnd(end3)
            track3.SetLayer(pcbnew.F_Cu)
            self.board.Add(track3)
        pcbnew.Refresh()
        self.logger.info('end:' )
        """

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
    