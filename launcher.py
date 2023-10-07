import bot
import asyncio
from dotenv import load_dotenv
import os


load_dotenv()

token = os.getenv("TOKEN")

bot = bot.Bot()

if __name__ == "__main__":
    asyncio.run(bot.load_cogs())

    bot.run(token)
