# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FootprintTextDialog
###########################################################################

class FootprintTextDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Footprint Text", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		fgSizer = wx.FlexGridSizer( 0, 5, 3, 0 )
		fgSizer.AddGrowableCol( 1 )
		fgSizer.AddGrowableCol( 4 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.textAttributes = wx.StaticText( self, wx.ID_ANY, u"Attributes:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textAttributes.Wrap( -1 )

		fgSizer.Add( self.textAttributes, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceAttributesChoices = []
		self.choiceAttributes = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceAttributesChoices, 0 )
		self.choiceAttributes.SetSelection( 0 )
		fgSizer.Add( self.choiceAttributes, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		fgSizer.Add( ( 0, 0), 0, wx.LEFT|wx.RIGHT, 40 )

		self.checkJustification = wx.CheckBox( self, wx.ID_ANY, u"Justification:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.checkJustification, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

		choiceJustificationChoices = []
		self.choiceJustification = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceJustificationChoices, 0 )
		self.choiceJustification.SetSelection( 0 )
		fgSizer.Add( self.choiceJustification, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.checkLayer = wx.CheckBox( self, wx.ID_ANY, u"toLayer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.checkLayer, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceLayerChoices = []
		self.choiceLayer = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceLayerChoices, 0 )
		self.choiceLayer.SetSelection( 0 )
		fgSizer.Add( self.choiceLayer, 0, wx.ALL, 5 )


		fgSizer.Add( ( 0, 0), 0, wx.LEFT|wx.RIGHT, 40 )

		self.checkOrientation = wx.CheckBox( self, wx.ID_ANY, u"Orientation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.checkOrientation, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

		choiceOrientationChoices = []
		self.choiceOrientation = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceOrientationChoices, 0 )
		self.choiceOrientation.SetSelection( 0 )
		fgSizer.Add( self.choiceOrientation, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.checkWidth = wx.CheckBox( self, wx.ID_ANY, u"Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.checkWidth, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editWidth = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.editWidth, 0, wx.ALL|wx.EXPAND, 5 )

		self.textUnitWith = wx.StaticText( self, wx.ID_ANY, u"unit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textUnitWith.Wrap( -1 )

		fgSizer.Add( self.textUnitWith, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.checkVisible = wx.CheckBox( self, wx.ID_ANY, u"Visible", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.checkVisible, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )


		fgSizer.Add( ( 0, 0), 0, 0, 5 )

		self.checkHeight = wx.CheckBox( self, wx.ID_ANY, u"Height:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.checkHeight, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editHeight = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.editHeight, 0, wx.ALL|wx.EXPAND, 5 )

		self.textUnitHeight = wx.StaticText( self, wx.ID_ANY, u"unit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textUnitHeight.Wrap( -1 )

		fgSizer.Add( self.textUnitHeight, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.checkItalic = wx.CheckBox( self, wx.ID_ANY, u"Italic", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.checkItalic, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.buttonClear = wx.Button( self, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.buttonClear, 0, wx.ALL|wx.EXPAND, 5 )

		self.checkThickness = wx.CheckBox( self, wx.ID_ANY, u"Thickness:", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.checkThickness, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editThickness = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.editThickness, 0, wx.ALL|wx.EXPAND, 5 )

		self.textUnitThickness = wx.StaticText( self, wx.ID_ANY, u"unit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textUnitThickness.Wrap( -1 )

		fgSizer.Add( self.textUnitThickness, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.checkMirrored = wx.CheckBox( self, wx.ID_ANY, u"Mirrored", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.checkMirrored, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.buttonUpdate = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.buttonUpdate, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( fgSizer, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 15 )

		self.staticline = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.staticline, 0, wx.EXPAND |wx.ALL, 5 )

		self.textLog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer1.Add( self.textLog, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


