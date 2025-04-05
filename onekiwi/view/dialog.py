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
## Class FanoutDialog
###########################################################################

class FanoutDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fanout Tools", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Create fanouts" ), wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.textSkip = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Skip:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textSkip.Wrap( -1 )
		fgSizer1.Add( self.textSkip, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		self.skip = wx.SpinCtrlDouble( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 2, 1 )
		self.skip.SetDigits( 0 )
		fgSizer1.Add( self.skip, 0, wx.ALL|wx.EXPAND, 5 )


		self.textFilttter = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Filtter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textFilttter.Wrap( -1 )

		fgSizer1.Add( self.textFilttter, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.editFiltter = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.editFiltter, 0, wx.ALL|wx.EXPAND, 5 )

		self.textReference = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Reference:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textReference.Wrap( -1 )

		fgSizer1.Add( self.textReference, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceReferenceChoices = []
		self.choiceReference = wx.Choice( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceReferenceChoices, 0 )
		self.choiceReference.SetSelection( 0 )
		fgSizer1.Add( self.choiceReference, 1, wx.ALL|wx.EXPAND, 5 )

		self.textTrack = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Track width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textTrack.Wrap( -1 )

		fgSizer1.Add( self.textTrack, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceTrackChoices = []
		self.choiceTrack = wx.Choice( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceTrackChoices, 0 )
		self.choiceTrack.SetSelection( 0 )
		fgSizer1.Add( self.choiceTrack, 1, wx.ALL|wx.EXPAND, 5 )

		self.textVia = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Via size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textVia.Wrap( -1 )

		fgSizer1.Add( self.textVia, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceViaChoices = []
		self.choiceVia = wx.Choice( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceViaChoices, 0 )
		self.choiceVia.SetSelection( 0 )
		fgSizer1.Add( self.choiceVia, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer5.Add( fgSizer1, 1, wx.EXPAND, 5 )

		self.checkUnusepad = wx.CheckBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Unused pads", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.checkUnusepad, 0, wx.ALL, 5 )


		bSizer8.Add( sbSizer5, 3, wx.BOTTOM|wx.EXPAND|wx.RIGHT, 5 )

		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Preview" ), wx.VERTICAL )

		self.bitmapPreview = wx.StaticBitmap( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.bitmapPreview, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( sbSizer6, 2, wx.BOTTOM|wx.EXPAND|wx.LEFT, 5 )


		bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )

		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Fanout length" ), wx.HORIZONTAL )

		self.checkUnlimited = wx.CheckBox( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Unlimited", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.checkUnlimited, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textMaximum = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Maximum:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textMaximum.Wrap( -1 )

		sbSizer7.Add( self.textMaximum, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editLength = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.editLength, 0, wx.ALL, 5 )

		self.textUnit = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"unit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textUnit.Wrap( -1 )

		sbSizer7.Add( self.textUnit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( sbSizer7, 0, wx.EXPAND, 5 )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Placement of via fanout for:" ), wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.textPackage = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Package:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textPackage.Wrap( -1 )

		bSizer9.Add( self.textPackage, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choicePackageChoices = []
		self.choicePackage = wx.Choice( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePackageChoices, 0 )
		self.choicePackage.SetSelection( 0 )
		bSizer9.Add( self.choicePackage, 0, wx.ALL, 5 )

		self.checkSpecial = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Special package:", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.checkSpecial, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceSpecialChoices = []
		self.choiceSpecial = wx.Choice( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceSpecialChoices, 0 )
		self.choiceSpecial.SetSelection( 0 )
		bSizer9.Add( self.choiceSpecial, 0, wx.ALL, 5 )


		sbSizer8.Add( bSizer9, 0, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		sizerAlignment = wx.BoxSizer( wx.VERTICAL )

		self.textAlignment = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Alignment:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textAlignment.Wrap( -1 )

		sizerAlignment.Add( self.textAlignment, 0, wx.ALL, 5 )

		choiceAlignmentChoices = []
		self.choiceAlignment = wx.Choice( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceAlignmentChoices, 0 )
		self.choiceAlignment.SetSelection( 0 )
		sizerAlignment.Add( self.choiceAlignment, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( sizerAlignment, 1, wx.EXPAND, 5 )

		sizerDirection = wx.BoxSizer( wx.VERTICAL )

		self.textDirection = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Direction:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textDirection.Wrap( -1 )

		sizerDirection.Add( self.textDirection, 0, wx.ALL, 5 )

		choiceDirectionChoices = []
		self.choiceDirection = wx.Choice( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceDirectionChoices, 0 )
		self.choiceDirection.SetSelection( 0 )
		sizerDirection.Add( self.choiceDirection, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( sizerDirection, 1, wx.EXPAND, 5 )

		sizerSpace = wx.BoxSizer( wx.VERTICAL )

		self.textSpace = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Spacing:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textSpace.Wrap( -1 )

		sizerSpace.Add( self.textSpace, 0, wx.ALL, 5 )

		choiceSpaceChoices = []
		self.choiceSpace = wx.Choice( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceSpaceChoices, 0 )
		self.choiceSpace.SetSelection( 0 )
		sizerSpace.Add( self.choiceSpace, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( sizerSpace, 1, wx.EXPAND, 5 )


		sbSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )


		bSizer5.Add( sbSizer8, 0, wx.EXPAND|wx.TOP, 5 )


		bSizer1.Add( bSizer5, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonFanout = wx.Button( self, wx.ID_ANY, u"Fanout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.buttonFanout, 1, wx.ALL|wx.EXPAND, 5 )

		self.buttonUndo = wx.Button( self, wx.ID_ANY, u"Undo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.buttonUndo, 1, wx.ALL|wx.EXPAND, 5 )

		self.buttonClear = wx.Button( self, wx.ID_ANY, u"Clear log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.buttonClear, 1, wx.ALL|wx.EXPAND, 5 )

		self.buttonClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.buttonClose, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer7, 0, wx.EXPAND, 5 )

		self.staticLine = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.staticLine, 0, wx.EXPAND |wx.ALL, 5 )

		self.textLog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer1.Add( self.textLog, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


