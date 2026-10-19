# The entrypoint into the application, parses any CLI arguments, establishes starting values and runs the application.
from session import Session
from session_manager import SessionManager
from data__displayer import DataDisplay
from user import User
from headless import HeadlessTest

class App:
	def __init__(self, REMOTE : bool, HEADLESS : bool):
		self.sm = None
		self.user = None
		self.session = None
		
		if REMOTE:
			self.user = User()
			self.sm = SessionManager(self.user)
		else:
			self.session = Session("Local Session", user = None)
	
		self.data_display = DataDisplay()
	
		if HEADLESS:
			HeadlessTest(self, verbosity = 3)

if __name__ == "__main__": 
	App(REMOTE = True, HEADLESS = True)