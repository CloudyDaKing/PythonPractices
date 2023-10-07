import discord
from discord import app_commands
from discord.ext import commands
from pymongo.server_api import ServerApi
import pymongo
from dotenv import load_dotenv
import os
from constants import uri

load_dotenv()

client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
database = client["database"]
quotes = database["quotes"]

class Quote:

    @staticmethod
    def quote_create(quote, interaction):
        quote_query = {"discordid": interaction.user.id, "quote": quote}
        quotes.insert_one(quote_query)
    @staticmethod
    def quote_search(userid):
        query = {"discordid": userid}
        returnquotes = quotes.find(query)
        embed = discord.Embed(title="all quotes")
        for x in returnquotes:
            x = x["quote"]
            embed.add_field(name="quote", value=x)
        return embed

    @staticmethod
    def random_quote():
        randomquote = quotes.aggregate([{'$sample': {'size': 1}}]).next()
        return randomquote["quote"]

class quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="quotecreate", description="Create a quote")
    async def quotecreate(self, interaction: discord.Interaction, quote: str):

        Quote.quote_create(quote, interaction)
        await interaction.response.send_message(f"quote created")

    @app_commands.command(name="quotesearch", description="Search for quotes from a specific user")
    async def quotesearch(self, interaction: discord.Interaction, user: discord.User):
        embed = Quote.quote_search(user.id)
        await interaction.response.send_message(embed=embed)


    @app_commands.command(name="randomquote", description="picks a random quote")
    async def randomquote(self, interation: discord.Interaction):
        randomisedquote = Quote.random_quote()
        embed = discord.Embed(title="Random quote", description=randomisedquote)
        await interation.response.send_message(embed = embed)




async def setup(bot):
    await bot.add_cog(quote(bot))