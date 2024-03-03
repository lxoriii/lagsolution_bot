from discord.ext import commands
from discord.commands import slash_command
import discord
from datetime import datetime


class ping(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command(description='Shows the current Bot Latency')
    async def ping(self, interaction: discord.Interaction):



        em = discord.Embed(
            title="Current Latence",
            description=f'**Latency:** {round(self.client.latency * 1000)}',
            color=discord.Color.green(),
            timestamp=datetime.now()
        )
        await interaction.response.send_message(embed=em)

def setup(client):
    client.add_cog(ping(client))