import discord
from datetime import datetime
from discord.ext import commands, tasks
from colorama import Fore
from discord.commands import slash_command, Option


class role(commands.Cog):

    def __init__(self, client):
        self.client = client


    @slash_command()
    @commands.has_role("Discord Bot Entwicklung")
    async def roleadd(self, interaction: discord.Interaction, role: Option(discord.Role)):
        member = interaction.user

        await member.add_roles(role)
        await interaction.response.send_message('Just better ig', ephemeral=True)
        
    @slash_command()
    @commands.has_role("Discord Bot Entwicklung")
    async def roleremove(self, interaction: discord.Interaction, role: Option(discord.Role)):
        member = interaction.user

        await member.remove_roles(role)
        await interaction.response.send_message('Just better ig', ephemeral=True)



def setup(client):
    client.add_cog(role(client))