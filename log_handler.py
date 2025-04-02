from pyrogram import Client, filters
from pyrogram.types import Message
from config import LOG_CHANNEL_ID

@Client.on_message(filters.private & filters.command("start"))
async def log_user(client, message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    username = f"@{message.from_user.username}" if message.from_user.username else "No Username"

    log_text = f"""
🚀 **New User Started the Bot!**
👤 **Name:** {user_name}
🔹 **User ID:** `{user_id}`
📌 **Username:** {username}
🕰 **Time:** {message.date}
"""
    await client.send_message(LOG_CHANNEL_ID, log_text)
