import discord
from discord.ext import commands
import os
import jishaku

intents = discord.Intents.all()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def load_cogs(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                cog_name = filename[:-3]
                await self.load_extension(f'cogs.{cog_name}')
                print(f"loaded {cog_name}")
        await self.load_extension("jishaku")


