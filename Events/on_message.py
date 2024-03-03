import discord
from discord.ext import commands


class on_message(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.Cog.listener()
    async def on_message(self, message):
        

        if 'nigger' in message.content or 'Nigger' in message.content or 'Niger' in message.content or 'niger' in message.content:
            await message.delete()


def setup(client):
    client.add_cog(on_message(client))