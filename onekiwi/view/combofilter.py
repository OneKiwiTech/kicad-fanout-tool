import wx

class FilterComboPopup(wx.ComboPopup):

    # overridden ComboPopup methods
    def __init__(self, combo):
        wx.ComboPopup.__init__(self)
        self.control = None
        self.combo = combo
        self.items = []
    
    def AddItem(self, txt):
        print('FilterComboPopup.AddItem')
        #self.lc.InsertItem(self.lc.GetItemCount(), txt)

    def OnMotion(self, event):
        print('FilterComboPopup.OnMotion')

    def OnLeftDown(self, event):
        print('FilterComboPopup.OnLeftDown')
        self.Dismiss()


    # The following methods are those that are overridable from the
    # ComboPopup base class.  Most of them are not required, but all
    # are shown here for demonstration purposes.


    # This is called immediately after construction finishes.  You can
    # use self.GetCombo if needed to get to the ComboCtrl instance.
    def Init(self):
        print('FilterComboPopup.Init')
        self.value = None
        #self.curitem = -1


    # Create the popup child control.  Return true for success.
    def Create(self, parent):
        print('FilterComboPopup.Create')
        self.control = wx.Panel(parent, wx.ID_ANY, style = wx.TAB_TRAVERSAL|wx.RAISED_BORDER)
        sizerMain = wx.BoxSizer(wx.VERTICAL)
        menu = wx.Menu()
        menu.Append(wx.ID_ABOUT, 'About')
        self.searchCtrl = wx.SearchCtrl(self.control, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
        self.searchCtrl.ShowSearchButton(True)
        self.searchCtrl.ShowCancelButton(True)
        self.searchCtrl.SetMinSize( wx.Size(-1, 35))
        self.searchCtrl.SetDescriptiveText('Filter')
        self.searchCtrl.SetMenu(menu)
        sizerMain.Add(self.searchCtrl, 0, wx.ALL|wx.EXPAND, 5)
        listFilterChoices = []
        self.listFilter = wx.ListBox(
            self.control, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listFilterChoices, 0)
        sizerMain.Add(self.listFilter, 1, wx.ALL|wx.EXPAND, 5)
        self.control.SetSizer(sizerMain)

        self.control.Bind(wx.EVT_MOTION, self.OnMotion)
        self.control.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.searchCtrl.Bind(wx.EVT_TEXT, self.OnTextChange)
        self.searchCtrl.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.listFilter.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDoubleClick)
        return True


    def OnLeftDoubleClick(self, event):
        print('OnLeftDoubleClick')
        self.value = event.GetEventObject().GetStringSelection()
        self.combo.SetValue(self.value)
    
    def OnTextChange(self, event):
        print('OnTextChange')
        value = event.GetEventObject().GetValue()
        self.listFilter.Clear()
        for item in self.items:
            if item.rfind(value) != -1:
                self.listFilter.Append(item)
    
    def OnSetFocus(self, event):
        print('OnSetFocus')
        self.searchCtrl.Clear()

    # Return the widget that is to be used for the popup
    def GetControl(self):
        print('FilterComboPopup.GetControl')
        return self.control

    # Called just prior to displaying the popup, you can use it to
    # 'select' the current item.
    def SetStringValue(self, val):
        print('FilterComboPopup.SetStringValue %s' %val)

    # Return a string representation of the current item.
    def GetStringValue(self):
        print('FilterComboPopup.GetStringValue')
        return "GetStringValue"

    # Called immediately after the popup is shown
    def OnPopup(self):
        print('FilterComboPopup.OnPopup')
        wx.ComboPopup.OnPopup(self)

    # Called when popup is dismissed
    def OnDismiss(self):
        print('FilterComboPopup.OnDismiss')
        wx.ComboPopup.OnDismiss(self)

    # This is called to custom paint in the combo control itself
    # (ie. not the popup).  Default implementation draws value as
    # string.
    def PaintComboControl(self, dc, rect):
        print('FilterComboPopup.PaintComboControl')
        wx.ComboPopup.PaintComboControl(self, dc, rect)

    # Receives key events from the parent ComboCtrl.  Events not
    # handled should be skipped, as usual.
    def OnComboKeyEvent(self, event):
        print('FilterComboPopup.OnComboKeyEvent')
        wx.ComboPopup.OnComboKeyEvent(self, event)

    # Implement if you need to support special action when user
    # double-clicks on the parent wxComboCtrl.
    def OnComboDoubleClick(self):
        print('FilterComboPopup.OnComboDoubleClick')
        wx.ComboPopup.OnComboDoubleClick(self)

    # Return final size of popup. Called on every popup, just prior to OnPopup.
    # minWidth = preferred minimum width for window
    # prefHeight = preferred height. Only applies if > 0,
    # maxHeight = max height for window, as limited by screen size
    #   and should only be rounded down, if necessary.
    def GetAdjustedSize(self, minWidth, prefHeight, maxHeight):
        print('FilterComboPopup.GetAdjustedSize: %d, %d, %d' % (minWidth, prefHeight, maxHeight))
        return wx.ComboPopup.GetAdjustedSize(self, minWidth, prefHeight, maxHeight)

    # Return true if you want delay the call to Create until the popup
    # is shown for the first time. It is more efficient, but note that
    # it is often more convenient to have the control created
    # immediately.
    # Default returns false.
    def LazyCreate(self):
        print('FilterComboPopup.LazyCreate')
        return wx.ComboPopup.LazyCreate(self)

class FilterCombo(wx.ComboCtrl):

    # overridden ComboCtrl methods
    def __init__(self, parent, id = wx.ID_ANY, choices = [], style = 0):
        wx.ComboCtrl.__init__(self, parent, id, pos = wx.DefaultPosition, style = style)
        self.panel = FilterComboPopup(self)
        self.SetPopupControl(self.panel)
        #self.SetValue('hala')
    
    def AddList(self, lists):
        self.panel.items = lists.copy()
        self.panel.listFilter.Append(lists)

    def SetSelection(self, n):
        print('\tFilterCombo.SetSelection')
        if n == -1:
            self.panel.SetStringValue("")

    def SetCategoryLabels(self, labels):
        print('\tFilterCombo.SetCategoryLabels')
        self.panel = FilterComboPopup(labels)
        self.SetPopupControl(self.panel)

    def SetCategoryValues(self, values):
        print('\tFilterCombo.SetCategoryValues')
        value = " ".join(values)
        self.SetValue(value)

    def GetCategoryValues(self):
        print('\tFilterCombo.GetCategoryValues')
        value = self.GetValue()
        return value