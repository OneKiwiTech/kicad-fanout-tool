from ..model.model import Model, Status
from ..view.view import FootprintTextView
from .logtext import LogText
import sys
import logging
import logging.config
import wx
import pcbnew
import math

class Controller:
    def __init__(self):
        self.view = FootprintTextView()
        self.logger = self.init_logger(None)
        self.logger = self.init_logger(self.view.textLog)
        status = self.get_current_status()
        self.model = Model(pcbnew.GetBoard(), status, self.logger)

        # Connect Events
        self.view.buttonUpdate.Bind(wx.EVT_BUTTON, self.OnButtonUpdate)
        self.view.buttonClear.Bind(wx.EVT_BUTTON, self.OnButtonClear)
        self.view.choiceAttributes.Bind( wx.EVT_CHOICE, self.OnChoiceAttributes)
        self.view.choiceJustification.Bind( wx.EVT_CHOICE, self.OnChoiceJustification)
        self.view.choiceLayer.Bind( wx.EVT_CHOICE, self.OnChoiceLayer)
        self.view.choiceOrientation.Bind( wx.EVT_CHOICE, self.OnChoiceOrientation)
        self.board = pcbnew.GetBoard()
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

    def OnButtonUpdate(self, event):
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
    
    def OnButtonClear(self, event):
        self.view.textLog.SetValue('')

    def OnChoiceAttributes(self, event):
        index = event.GetEventObject().GetSelection()
        value = event.GetEventObject().GetString(index)
        if value in ['B.Silk_Reference', 'B.Fab_Reference', 'B.Footprint_Value']:
            self.view.SetMirror(True)
        else:
            self.view.SetMirror(False)
        self.logger.info('Selected: %s' %value)

    def OnChoiceJustification(self, event):
        index = event.GetEventObject().GetSelection()
        value = event.GetEventObject().GetString(index)
        self.logger.info('Selected: %s' %value)
    
    def OnChoiceLayer(self, event):
        index = event.GetEventObject().GetSelection()
        value = event.GetEventObject().GetString(index)
        self.logger.info('Selected: %s' %value)
    
    def OnChoiceOrientation(self, event):
        index = event.GetEventObject().GetSelection()
        value = event.GetEventObject().GetString(index)
        self.logger.info('Selected: %s' %value)

    def get_current_status(self):
        attribute = self.view.GetAttributesValue()
        layer = self.view.GetLayerValue()
        orientation = self.view.GetOrientationValue()
        justification = self.view.GetJustificationValue()
        width = self.view.GetWidthValue()
        height = self.view.GetHeightValue()
        thickness = self.view.GetThicknessValue()
        checkLayer = self.view.GetLayerChecked()
        checkWidth = self.view.GetWidthChecked()
        checkHeight = self.view.GetHeightChecked()
        checkThickness = self.view.GetThicknessChecked()
        checkJustification = self.view.GetJustificationChecked()
        checkOrientation = self.view.GetOrientationChecked()
        visible = self.view.GetVisibleChecked()
        italic = self.view.GetItalicChecked()
        mirrored = self.view.GetMirroredChecked()
        status = Status(
            attribute, layer, checkLayer, width, checkWidth, 
            height, checkHeight, thickness, checkThickness, 
            justification, checkJustification, orientation, 
            checkOrientation, visible, italic, mirrored
        )
        return status

    def init_logger(self, texlog):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        # Log to stderr
        #handler1 = logging.StreamHandler(sys.stderr)
        #handler1.setLevel(logging.DEBUG)
        # and to our GUI
        handler2 = LogText(texlog)
        handler2.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(funcName)s -  %(message)s",
            datefmt="%Y.%m.%d %H:%M:%S",
        )
        #handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)
        #root.addHandler(handler1)
        root.addHandler(handler2)
        return logging.getLogger(__name__)
    