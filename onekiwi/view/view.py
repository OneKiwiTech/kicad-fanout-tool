import wx
from .dialog import *
from ..version import version

class FanoutView(FanoutDialog):
    def __init__(self):
        FanoutDialog.__init__(self, None)
        self.SetTitle('Fanout Tool v%s' % version) 