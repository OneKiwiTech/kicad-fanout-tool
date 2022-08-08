import wx
import pcbnew
from onekiwi.controller.controller import Controller

filename = '/home/vanson/working/kicad/radio-4g-imx-rt1052/iMXRT1052_Thatico.kicad_pcb'

class PluginApp(wx.App):
    def OnInit(self):
        board = pcbnew.LoadBoard(filename)
        controller = Controller(board)
        controller.Show()
        return True

def main():
    app = PluginApp()
    app.MainLoop()

    print("Done")

if __name__ == "__main__":
    main()