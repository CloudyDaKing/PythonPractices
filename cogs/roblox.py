import discord
from discord import app_commands
from discord.ext import commands

class Roblox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="devex", description="Check DevEx Rates")
    async def devex(self, interaction: discord.Interaction, robux:int):

        embed = discord.Embed(title=f"DevEx Rates For {robux} Robux",
                              colour=0x006eff)
        devxrate = round(robux * 0.0035, 2)
        embed.add_field(name="DevEx",
                        value=f"${devxrate}",
                        inline=True)
        aftertax = round(robux / 0.7, 0)
        embed.add_field(name="After Tax",
                        value=f"{aftertax} robux",
                        inline=True)
        overall = round(aftertax * 0.0035, 2)
        embed.add_field(name="After Tax & DevEx",
                        value=f"${overall}",
                        inline=False)

        embed.set_footer(text="Does not count for conversion fees")

        await interaction.response.send_message(embed=embed)
async def setup(bot):
    await bot.add_cog(Roblox(bot))