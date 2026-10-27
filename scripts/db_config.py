# Contains configuration settings for the database connection
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

DB_NAME = "des_app"
SESSION_COLLECTION = "sessions"
USER_COLLECTION = "users"