import wx
from .dialog import *
from ..kicad.board import get_current_unit
from ..version import version

class FootprintTextView(FootprintTextDialog):
    def __init__(self):
        FootprintTextDialog.__init__(self, None)
        self.SetTitle('Fanout Tool v%s' % version)
        self.AddItemAttributes()
        self.AddItemJustification()
        self.AddItemLayer()
        self.AddItemOrientation()
        self.window = wx.GetTopLevelParent(self)
        self.SetVisible(True)
        self.SetUnit()
        #self.textLog.SetMinSize(self.HighResWxSize(self.window, wx.Size(-1, 150)))
        
    def AddItemAttributes(self):
        items = [
            'F.Silk_Reference', 'B.Silk_Reference', 
            'F.Fab_Reference', 'B.Fab_Reference', 
            'F.Footprint_Value', 'B.Footprint_Value']
        self.choiceAttributes.Append(items)
        self.choiceAttributes.SetSelection(0)

    def AddItemJustification(self):
        items = ['Left', 'Center', 'Right']
        self.choiceJustification.Append(items)
        self.choiceJustification.SetSelection(0)
    
    def AddItemLayer(self):
        items = [
            'F.Silkscreen', 'B.Silkscreen',
            'F.Fab', 'B.Fab', 'F.Cu', 'B.Cu',
            'User.1', 'User.2','User.3',
            'User.4', 'User.5', 'User.6',
            'User.7', 'User.8', 'User.9']
        self.choiceLayer.Append(items)
        self.choiceLayer.SetSelection(0)
    
    def AddItemOrientation(self):
        items = [
            '0.0', '45.0', '90.0', '135.0', '180.0',
            '-45.0', '-90.0', '-135.0', '-180.0']
        self.choiceOrientation.Append(items)
        self.choiceOrientation.SetSelection(4)

    def SetUnit(self):
        unit = get_current_unit()
        self.textUnitWith.LabelText = unit
        self.textUnitHeight.LabelText = unit
        self.textUnitThickness.LabelText = unit
    
    
    def GetAttributesValue(self):
        index = self.choiceAttributes.GetSelection()
        value = self.choiceAttributes.GetString(index)
        return value
    
    def GetJustificationValue(self):
        index = self.choiceJustification.GetSelection()
        value = self.choiceJustification.GetString(index)
        justify = 0
        if value == 'Left':
            justify = -1
        elif value == 'Right':
            justify = 1
        else:
            justify = 0
        return justify
    
    def GetLayerValue(self):
        index = self.choiceLayer.GetSelection()
        value = self.choiceLayer.GetString(index)
        return value
    
    def GetOrientationValue(self):
        index = self.choiceOrientation.GetSelection()
        value = self.choiceOrientation.GetString(index)
        angle = 10*float(value)
        return angle
    
    def GetWidthValue(self):
        return self.editWidth.GetValue()

    def GetHeightValue(self):
        return self.editHeight.GetValue()

    def GetThicknessValue(self):
        return self.editThickness.GetValue()

    def GetThicknessChecked(self):
        return self.checkThickness.GetValue()

    def GetHeightChecked(self):
        return self.checkHeight.GetValue()

    def GetItalicChecked(self):
        return self.checkItalic.GetValue()

    def GetJustificationChecked(self):
        return self.checkJustification.GetValue()

    def GetLayerChecked(self):
        return self.checkLayer.GetValue()

    def GetMirroredChecked(self):
        return self.checkMirrored.GetValue()

    def GetVisibleChecked(self):
        return self.checkVisible.GetValue()

    def GetWidthChecked(self):
        return self.checkWidth.GetValue()

    def GetOrientationChecked(self):
        return self.checkOrientation.GetValue()
    
    def SetMirror(self, value):
        return self.checkMirrored.SetValue(value)

    def SetVisible(self, value):
        return self.checkVisible.SetValue(value)

    def HighResWxSize(self, window, size):
        """Workaround if wxWidgets Version does not support FromDIP"""
        if hasattr(window, "FromDIP"):
            return window.FromDIP(size)
        else:
            return size