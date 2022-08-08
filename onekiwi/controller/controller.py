from ..kicad.board import get_image_path
from ..model.model import Model
from ..view.view import FanoutView
from .logtext import LogText
import sys
import logging
import logging.config
import wx
import pcbnew
from .package import get_packages
import os

class Controller:
    def __init__(self, board):
        self.view = FanoutView()
        self.board = board
        self.reference = None
        self.tracks = []
        self.vias = []
        self.packages = get_packages()
        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(self.board, self.logger)

        # Connect Events
        self.view.buttonFanout.Bind(wx.EVT_BUTTON, self.OnButtonFanout)
        self.view.buttonUndo.Bind(wx.EVT_BUTTON, self.OnButtonUndo)
        self.view.buttonClear.Bind(wx.EVT_BUTTON, self.OnButtonClear)
        self.view.buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonClose)
        self.view.choicePackage.Bind( wx.EVT_CHOICE, self.OnChoicePackage)
        self.view.choiceAlignment.Bind( wx.EVT_CHOICE, self.OnChoiceAlignment)
        self.view.choiceDirection.Bind( wx.EVT_CHOICE, self.OnChoiceDirection)
        
        self.add_references()
        self.get_tracks_vias()
        self.set_package()

        path = get_image_path()
        image = os.path.join(path, 'image.svg')
        self.view.SetImagePreview(image)

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
        package = self.view.GetPackageValue()
        alignment = self.view.GetAlignmentValue()
        direction = self.view.GetDirectionValue()
        self.model.update_data(reference, self.tracks[track_index], self.vias[via_index])
        self.model.update_package(package, alignment, direction)
        self.model.fanout()

    def OnButtonUndo(self, event):
        self.model.remove_track_via()

    def OnButtonClear(self, event):
        self.view.textLog.SetValue('')

    def OnButtonClose(self, event):
        self.Close()

    def OnChoicePackage(self, event):
        index = event.GetEventObject().GetSelection()
        value = event.GetEventObject().GetString(index)
        package = self.packages[index]
        alignments = []
        directions = []
        for i, ali in enumerate(package.alignments, 0):
            alignments.append(ali.name)
            if i == 0:
                directions = ali.directions.copy()
        self.view.ClearAlignment()
        self.view.ClearDirection()
        if value == 'BGA staggered':
            alignments.clear()
        self.view.AddAlignment(alignments)
        self.view.AddDirection(directions)

    def OnChoiceAlignment(self, event):
        align_i = event.GetEventObject().GetSelection()
        pack_i = self.view.GetPackageIndex()
        directions = self.packages[pack_i].alignments[align_i].directions
        self.view.ClearDirection()
        self.view.AddDirection(directions)

    def OnChoiceDirection(self, event):
        index = event.GetEventObject().GetSelection()
        value = event.GetEventObject().GetString(index)

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

    def set_package(self):
        default = 2 #bga
        packages = []
        alignments = []
        for package in self.packages:
            packages.append(package.name)
            if package.name == 'BGA':
                for alig in package.alignments:
                    alignments.append(alig.name)
        self.view.AddPackageType(packages, default)
        self.view.AddAlignment(alignments)

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
    