#  Connects to the database and saves/loads data.
from pymongo import MongoClient
import config
from message import Message

class DatabaseConnection:
	def __init__(self):
		self.client = MongoClient(config.MONGO_URI)
		self.client.admin.command("ping")
	
	
	def get_collection(self, collection):
		"""Retrieve a specific collection from the remote database."""
		return self.client[config.DB_NAME][collection]
	
	
	def wipe_data(self, session):
		"""Attempt to completely remove the given session from the database"""
		if not session:
			return "Invalid session"

		self.get_collection(config.SESSION_COLLECTION).delete_one({"session": session.session_name})
		return "Session wiped successfully"
	
	
	def push_data(self, session):
		"""Attempt to replace the remote data for the current session with the local data of the current session. If the session does not exist, a new one will be created."""
		if not session:
			return "Invalid session"
  
		messages = []
  
		for message in session._chat.messages:
			messages.append({"sender": message.sender, "contents": message.contents})
  
		formatted_data = { "session": session.session_name, "datasets": session._files.internal_db, "chat":  messages}
  
		return self.get_collection(config.SESSION_COLLECTION).find_one_and_replace({"session": session.session_name}, formatted_data, upsert=True)


	def pull_data(self, session):
		"""Attempts to retrieve the data for the current session and assign it back onto itself, effectively updating it to match the remote data."""
		if not session:
			return "Invalid session"

		pulled_data = self.get_collection(config.SESSION_COLLECTION).find_one({"session": session.session_name})

		if not pulled_data:
			return "No corelating session in database"

		pulled_datasets = []
		pulled_messages = []
	
		for datasource in pulled_data['datasets']:
			if datasource['dataset'] not in pulled_datasets:
				pulled_datasets.append(datasource['dataset'])
		
		for message in pulled_data["chat"]:
			pulled_messages.append(Message(message['sender'], message['contents']))
 
		session.session_name = pulled_data['session']
		session._files.datasets = pulled_datasets
		session._files.internal_db = pulled_data['datasets']
		session._chat.messages = pulled_messages

		return "Session pulled successfully"


	def get_all_sessions(self):
		"""Retrieves all session documents from the remote database."""
		return self.get_collection(config.SESSION_COLLECTION).find()