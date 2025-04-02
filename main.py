from pyrogram import Client  
import config  

bot = Client(  
    "ReactionBot",  
    api_id=config.API_ID,  
    api_hash=config.API_HASH,  
    bot_token=config.BOT_TOKEN  
)  

if __name__ == "__main__":  
    bot.run()
