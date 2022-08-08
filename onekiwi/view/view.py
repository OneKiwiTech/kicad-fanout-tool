import wx
from .dialog import *
from ..version import version

class FanoutView(FanoutDialog):
    def __init__(self):
        FanoutDialog.__init__(self, None)
        self.SetTitle('Fanout Tool v%s' % version)
    
    def AddReferences(self, references):
        self.choiceReference.AddList(references)

    def GetReferenceSelected(self):
        return self.choiceReference.GetCategoryValues()

    def AddTracksWidth(self, tracks):
        self.choiceTrack.Append(tracks)
        self.choiceTrack.SetSelection(0)

    def AddViasSize(self, vias):
        self.choiceVia.Append(vias)
        self.choiceVia.SetSelection(0)

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
    
    def AddAlignment(self, items):
        self.choiceAlignment.Append(items)
        self.choiceAlignment.SetSelection(0)
    
    def ClearAlignment(self):
        self.choiceAlignment.Clear()
    
    def GetAlignmentIndex(self):
        index = self.choiceAlignment.GetSelection()
        return index
    
    def AddDirection(self, items):
        self.choiceDirection.Append(items)
        self.choiceDirection.SetSelection(0)
    
    def ClearDirection(self):
        self.choiceDirection.Clear()
    
    def GetDirectionIndex(self):
        index = self.choiceDirection.GetSelection()
        return index