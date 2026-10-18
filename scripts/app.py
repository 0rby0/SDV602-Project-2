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
			self.sm = SessionManager()
			self.user = User()
		else:
			self.session = Session("Local Session", remote=False)
	
		self.data_display = DataDisplay()
	
		if HEADLESS:
			HeadlessTest(self, True)

if __name__ == "__main__": 
	App(REMOTE=False, HEADLESS=True)