from pyrogram import Client, filters  
from random import choice  

REACTIONS = ["😂", "🔥", "😍", "😎", "💀"]  

@Client.on_message(filters.text & ~filters.bot)  
async def react(client, message):  
    reaction = choice(REACTIONS)  
    await message.react(reaction)
