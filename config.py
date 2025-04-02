import os  

BOT_TOKEN = os.getenv("BOT_TOKEN")  
API_ID = int(os.getenv("API_ID", 0))  
API_HASH = os.getenv("API_HASH")  
MONGO_URI = os.getenv("MONGO_URI")  
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))  
FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL")
