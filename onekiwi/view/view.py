import wx
from .dialog import *
from ..version import version
import os
from ..kicad.board import get_image_path

class FanoutView(FanoutDialog):
    def __init__(self):
        FanoutDialog.__init__(self, None)
        self.SetTitle('Fanout Tool v%s' % version)
    def GetSkipIndex(self):
        return int(self.skip.GetValue())
    
    def AddReferences(self, references):
        self.choiceReference.Append(references)

    def SetIndexReferences(self, index):
        self.choiceReference.SetSelection(index)

    def ClearReferences(self):
        self.choiceReference.Clear()

    def GetReferenceSelected(self):
        index = self.choiceReference.GetSelection()
        value = self.choiceReference.GetString(index)
        return value
    def AddTracksWidth(self, tracks):
        self.choiceTrack.Append(tracks)
        self.choiceTrack.SetSelection(0)

    def AddViasSize(self, vias):
        self.choiceVia.Append(vias)
        self.choiceVia.SetSelection(0)
    def GetCheckUnusepad(self):
        return self.checkUnusepad.GetValue()

    def GetTrackSelectedIndex(self):
        return self.choiceTrack.GetSelection()

    def GetViaSelectedIndex(self):
        return self.choiceVia.GetSelection()

    def AddPackageType(self, items, index):
        self.choicePackage.Append(items)
        self.choicePackage.SetSelection(index)

    def GetPackageIndex(self):
        index = self.choicePackage.GetSelection()
        return index
    
    def GetPackageValue(self):
        index = self.choicePackage.GetSelection()
        value = self.choicePackage.GetString(index)
        return value
    
    def AddAlignment(self, items):
        self.choiceAlignment.Append(items)
        self.choiceAlignment.SetSelection(0)
    
    def ClearAlignment(self):
        self.choiceAlignment.Clear()
    
    def GetAlignmentIndex(self):
        index = self.choiceAlignment.GetSelection()
        return index
    
    def GetAlignmentValue(self):
        index = self.choiceAlignment.GetSelection()
        value = self.choiceAlignment.GetString(index)
        return value
    
    def AddDirection(self, items):
        self.choiceDirection.Append(items)
        self.choiceDirection.SetSelection(0)
    
    def ClearDirection(self):
        self.choiceDirection.Clear()
    
    def GetDirectionIndex(self):
        index = self.choiceDirection.GetSelection()
        return index
    
    def GetDirectionValue(self):
        index = self.choiceDirection.GetSelection()
        print(index)
        value = self.choiceDirection.GetString(index)
        return value
    
    def SetImagePreview(self, name):
        path = get_image_path()
        image = os.path.join(path, name)
        self.bitmapPreview.SetBitmap(wx.Bitmap(image))