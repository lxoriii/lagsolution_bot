import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from datetime import datetime

class ui(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command(description='Siehe information von einem user')
    async def userinfo(self, ctx, user: Option(discord.User, 'Der User dessen Information du haben willst', required=False) = None):
        if user == None:
            userinfo = discord.Embed(
                title=f'Userinfo von {ctx.author.name}',
                color=0x0b83f3,
                timestamp=datetime.now()
            )
            userinfo.add_field(
                name='General',
                value=f"""
                        > **Member:** {ctx.author.name}#{ctx.author.discriminator}
                        > **ID:** `{ctx.author.id}`
                        > **Mention:** {ctx.author.mention}
                        > **Nickname:** `{(ctx.author.nick if ctx.author.nick else "No Nickname")}`
                        > **Farbe:** `{ctx.author.color}`
                        > **Höchste Rolle:** {ctx.author.top_role.mention}
                        """
                        )
            
            userinfo.add_field(
                name='Discord',
                value=f"""
                        > **Account erstellt am:** {discord.utils.format_dt(ctx.author.created_at)}
                        > **Server beigetreten am:** {discord.utils.format_dt(ctx.author.joined_at)}
                       """,
                inline=False
            )

            userinfo.set_thumbnail(url=ctx.author.avatar)

            await ctx.respond(embed=userinfo, ephemeral=True)

        else:
            userinfo = discord.Embed(
                title=f'Userinfo von {ctx.author.name}',
                color=0x0b83f3,
                timestamp=datetime.now()
            )
            userinfo.add_field(
                name='General',
                value=f"""
                        > **Member:** {ctx.author.name}#{ctx.author.discriminator}
                        > **ID:** `{ctx.author.id}`
                        > **Mention:** {ctx.author.mention}
                        > **Nickname:** `{(ctx.author.nick if ctx.author.nick else "No Nickname")}`
                        > **Farbe:** `{ctx.author.color}`
                        > **Höchste Rolle:** {ctx.author.top_role.mention}
                        """
                        )
            
            userinfo.add_field(
                name='Discord',
                value=f"""
                        > **Account erstellt am:** {discord.utils.format_dt(ctx.author.created_at)}
                        > **Server beigetreten am:** {discord.utils.format_dt(ctx.author.joined_at)}
                       """,
                inline=False
            )

            userinfo.set_thumbnail(url=user.avatar)

            await ctx.respond(embed=userinfo, ephemeral=True)


def setup(client):
    client.add_cog(ui(client))