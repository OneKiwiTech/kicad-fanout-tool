import pcbnew
import os
from .controller.controller import Controller

class FanoutAction(pcbnew.ActionPlugin):
	def defaults(self):
		self.name = "Fanout Tools"
		self.category = "Modify PCB"
		self.description = "BGA fanout routing"
		self.show_toolbar_button = True # Optional, defaults to False
		self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png') # Optional

	def Run(self):
		# The entry function of the plugin that is executed on user action
		board = pcbnew.GetBoard()
		controller = Controller(board)
		controller.Show()
		pcbnew.UpdateUserInterface()
FanoutAction().register() # Instantiate and register to Pcbnew
       
