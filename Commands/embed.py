from discord.ext import commands
from discord.commands import slash_command
from Views.EmModal import EmbedSetup

class embed(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command(description='Sende ein Embed')
    @commands.has_role('➤╏Lag Solution')
    async def sayembed(
            self, interaction
        ):
        
        await interaction.response.send_modal(EmbedSetup(title=f'Embed Builder'))



def setup(client):
    client.add_cog(embed(client))