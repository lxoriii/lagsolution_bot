from discord.ext import commands
from discord.commands import slash_command  ,  Option




class purge(commands.Cog):

    def __init__(self, client):
        self.client = client

    @slash_command(description='Lösche eine bestimmte anzahl an Nachrichten')
    @commands.has_role('➤╏Lag Solution')
    async def purge(self, ctx, amount: Option(int)):

        deleted = await ctx.channel.purge(limit=amount)
        await ctx.respond('`Succesfully Cleared {} Message(s)`'.format(len(deleted)), delete_after=3)



def setup(client):
     client.add_cog(purge(client))