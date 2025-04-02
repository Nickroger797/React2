from pyrogram import Client, filters
from pyrogram.types import Message
from config import FORCE_SUB_CHANNEL

async def is_subscribed(client: Client, user_id: int):
    try:
        member = await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

@Client.on_message(filters.private & filters.command("start"))
async def start_command(client, message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    if not await is_subscribed(client, user_id):
        await message.reply_text(
            f"🔔 पहले हमारे चैनल को जॉइन करें!\n\n[Join Now](https://t.me/{FORCE_SUB_CHANNEL})",
            disable_web_page_preview=True
        )
        return
    
    await message.reply_text(f"👋 Welcome {user_name}!\n\nआपका स्वागत है!")
