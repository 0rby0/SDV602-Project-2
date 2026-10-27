# Manage users in the database
from pymongo import MongoClient
import db_config as db_config

class UserManager:
	def __init__(self):
		self.client = MongoClient(db_config.MONGO_URI)
		self.client.admin.command("ping")
  
  
	def get_collection(self, collection):
		"""Gets the specified collection from the remote database."""
		return self.client[db_config.DB_NAME][collection]
	
 
	def find_user(self, username):
		"""Finds the account with the given name from the remote database."""
		return self.get_collection(db_config.USER_COLLECTION).find_one({"username": username})


	def create_user(self, username, hash):
		"""Add a new account to the database with a hashed password."""
		userdata = {"username": username, "hash": hash}
		self.get_collection(db_config.USER_COLLECTION).insert_one(userdata)
		return "User created successfully"


	def wipe_user(self, username):
		"""Wipes the user's data from the database"""
		if not self.find_user(username):
			return "User not in database"

		self.get_collection(db_config.USER_COLLECTION).delete_one({"username": username})
		return "User removed from database"