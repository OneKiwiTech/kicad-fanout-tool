import pcbnew
import os
import sys
import logging
import tempfile
from .controller.controller import Controller

class LengthMatchingAction(pcbnew.ActionPlugin):
	def defaults(self):
		self.name = "Fanout Tools"
		self.category = "Modify PCB"
		self.description = "Edit reference value on layer Silkscreen and Fabrication"
		self.show_toolbar_button = True # Optional, defaults to False
		self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png') # Optional

	def Run(self):
		# The entry function of the plugin that is executed on user action
		self.InitLogger()
		self.logger = logging.getLogger(__name__)
		#if controller.Show() == wx.ID_OK:
		controller = Controller()
		controller.Show()
		pcbnew.UpdateUserInterface()

	def InitLogger(self):
		root = logging.getLogger()
		root.setLevel(logging.DEBUG)

		# Log to stderr
		handler1 = logging.StreamHandler(sys.stderr)
		handler1.setLevel(logging.DEBUG)


		log_path = os.path.dirname(__file__)
		log_file = os.path.join(log_path, "error.log")

		# and to our error file
		# Check logging file permissions, if fails, move log file to tmp folder
		handler2 = None
		try:
			handler2 = logging.FileHandler(log_file)
		except PermissionError:
			log_path = os.path.join(tempfile.mkdtemp()) 
		try: # Use try/except here because python 2.7 doesn't support exist_ok
			os.makedirs(log_path)

		except:
			pass
		log_file = os.path.join(log_path, "debug.log")
		handler2 = logging.FileHandler(log_file)

		# Also move config file
		self.config_file = os.path.join(log_path, 'config.json')

		handler2.setLevel(logging.DEBUG)
		formatter = logging.Formatter(
		"%(asctime)s %(name)s %(lineno)d:%(message)s", datefmt="%m-%d %H:%M:%S"
		)
		handler1.setFormatter(formatter)
		handler2.setFormatter(formatter)
		root.addHandler(handler1)
		root.addHandler(handler2)
       
