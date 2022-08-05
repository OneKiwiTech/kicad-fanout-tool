import wx
from onekiwi.controller.controller import Controller

class SimplePluginApp(wx.App):
    def OnInit(self):
        controller = Controller()
        controller.Show()
        return True

def main():
    app = SimplePluginApp()
    app.MainLoop()

    print("Done")

if __name__ == "__main__":
    main()