try:
    import pcbnew
except:
    import sys
    sys.path.insert(0,"/usr/lib/python3.8/site-packages/")
    import pcbnew
import wx

from onekiwi.controller.controller import Controller

filename = '/home/vanson/working/kicad/onekiwi/som-imx8qxp-fbga609/som-imx8qxp-fbga609.kicad_pcb'

class SimplePluginApp(wx.App):
    def OnInit(self):
        try:
            board = pcbnew.LoadBoard(filename)
            controller = Controller(board)
            controller.Show()
            return True
        except OSError:
            print("OSError: Unable to open file for reading.")
            return 0

def main():
    app = SimplePluginApp()
    app.MainLoop()

    print("Done")

if __name__ == "__main__":
    main()