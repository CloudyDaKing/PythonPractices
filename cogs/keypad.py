import discord
from discord import app_commands
from discord.ext import commands


class KeypadView(discord.ui.View):
    def __init__(self, interaction):
        super().__init__()
        self.code = []

    async def update_message(self, interaction):
        new_content = " ".join(self.code)
        if not new_content:
            new_content = "Enter code..."
        await interaction.response.edit_message(content=new_content)

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.code.append("0")
        await self.update_message(interaction)

    @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.code.append("1")
        await self.update_message(interaction)

    @discord.ui.button(label="2", style=discord.ButtonStyle.gray)
    async def button3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.code.append("2")
        await self.update_message(interaction)

    @discord.ui.button(label="3", style=discord.ButtonStyle.gray)
    async def button4(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.code.append("3")
        await self.update_message(interaction)

    @discord.ui.button(label="4", style=discord.ButtonStyle.gray)
    async def button5(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.code.append("4")
        await self.update_message(interaction)

    @discord.ui.button(label="5", style=discord.ButtonStyle.gray)
    async def button6(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.code.append("5")
        await self.update_message(interaction)

    @discord.ui.button(label="6", style=discord.ButtonStyle.gray)
    async def button7(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.code.append("6")
        await self.update_message(interaction)

    @discord.ui.button(label="7", style=discord.ButtonStyle.gray)
    async def button8(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.code.append("7")
        await self.update_message(interaction)

    @discord.ui.button(label="8", style=discord.ButtonStyle.gray)
    async def button9(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.code.append("8")
        await self.update_message(interaction)

    @discord.ui.button(label="9", style=discord.ButtonStyle.gray)
    async def button11(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.code.append("9")
        await self.update_message(interaction)

    @discord.ui.button(label="backspace", style=discord.ButtonStyle.red)
    async def button10(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.code.pop()
        await self.update_message(interaction)

    @discord.ui.button(label="Done", style=discord.ButtonStyle.green)
    async def button12(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.code != [6, 9, 6, 9]:
            await interaction.response.edit_message(content="Incorrect password try again")
            self.code = []
            await self.update_message(interaction)
        else:
            await interaction.response.edit_message(content="correct")


class Keypad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="keypad", description="yes")
    async def keypad(self, interaction: discord.Interaction):
        attempt = KeypadView(interaction)
        await interaction.response.send_message("keypad", view=attempt)


async def setup(bot):
    await bot.add_cog(Keypad(bot))
