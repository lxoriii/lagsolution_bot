import discord
from colorama import Fore
from discord.ext import commands
from discord.commands import Option
from discord.commands import slash_command

class Lockunlock(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @slash_command(description="Lock a channel!")
    @commands.has_role('➤╏Lag Solution')
    async def lock(self, ctx):
        embed = discord.Embed(
            description=" 🔒 **Channel Locked**",
            color=16711680,
            timestamp=discord.utils.utcnow()
        )
        embed.set_footer(
            text=f"{ctx.author.name}",
            icon_url=ctx.author.avatar.url
        )
        try:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        except discord.Forbidden:
            await ctx.respond("I don't have permission")
            return
        await ctx.respond(embed=embed)

    @slash_command(description="Unlock a channel!")
    @commands.has_role('➤╏Lag Solution')
    async def unlock(self, ctx):
        embed = discord.Embed(
            description=" 🔓 **Channel unlocked**",
            color=65290,
            timestamp=discord.utils.utcnow()
        )
        embed.set_footer(
            text=f"{ctx.author.name}",
            icon_url=ctx.author.avatar.url
        )
        try:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        except discord.Forbidden:
            await ctx.respond("I don't have permission", ephemeral=True)
            return
        await ctx.respond(embed=embed)



def setup(client):
    client.add_cog(Lockunlock(client))