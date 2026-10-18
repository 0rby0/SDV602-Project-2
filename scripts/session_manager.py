# Create, Delete, and load sessions
from database_connect import DatabaseConnection
from session import Session

class SessionManager:
	def __init__(self):
		self.sessions = []
		self.db = DatabaseConnection()


	def get_remote_sessions(self):
		"""Retrieves and returns the names of all remote sessions being stored in the database."""
		session_list = []
		retrieved_sessions = self.db.get_all_sessions()

		if not retrieved_sessions:
			return "No sessions"
  
		for session in retrieved_sessions:
			session_list.append(session["session"])

		return session_list


	def join_or_create_session(self, session_name):
		"""Creates a new session in the sessions list, if the session exists in the database it will find itself."""
		self.sessions.append(Session(session_name, True))
		return f"Successfully joined session: '{session_name}'"


	def leave_session(self, session_name):
		"""Attempt to remove the session with the requested name from the session manager session list"""
		session_index = 0

		# Check if each session is the one being requested
		for session in self.sessions:
			if session_name == session.session_name:
				# Delete the current index from the main list if the names match
				self.sessions.remove(self.sessions[session_index])
				return "Successfully left session"
			else:
				# Increase the index if the names don't match
				session_index += 1
   
		# Only show the error message if none of the names match
		return "Not in session"
		
		