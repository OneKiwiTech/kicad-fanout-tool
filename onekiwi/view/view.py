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