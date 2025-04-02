import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL")  # चैनल का Username (Without @)
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))  # Log Channel ID
