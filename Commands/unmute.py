from discord.ext import commands
from discord.commands import slash_command  ,  Option
import discord  ,  asyncio
from datetime import datetime, timedelta
import asyncio


class unmute(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command(description='Unmute eine User')
    @commands.has_role('➤╏Lag Solution')
    async def unmute(self, interaction: discord.Interaction,
        member: Option(discord.User, "Unmute einen user", required=True),
    ):

        await interaction.response.defer()
        await asyncio.sleep(1)

        try:
            em = discord.Embed(
                title=f'Unmuted {member.name}!',
                description=f'┌› 🔹〢 Moderator: {interaction.user.mention}\n'
                            f'├› 🔹〢 Moderator ID: `{interaction.user.id}`\n'
                            f'├› 🔹〢 In Guild: `{interaction.guild.name}`\n'
                            f'├› 🔹〢 User: {member.mention}\n'
                            f'├› 🔹〢 ID: `{member.id}`\n'
                            f'└› 🔹〢 Action: **Unmute**\n',
                color=0xee00e3,
                timestamp=datetime.now()
            )
            em.set_footer(text="Bot Created by Ƒʉͫcͧкͭιͪηͣ dbxflame#4141")
            await interaction.followup.send(embed=em)
            await member.remove_timeout()


        except:

            em1 = discord.Embed(
                title=f'Error',
                description=f'I wasnt able to mute {member.mention}. \n`MISSING_PERMISSION`',
                color=0xee00e3,
                timestamp=datetime.now()
            )

            await interaction.followup.send(embed=em1, ephemeral=True)
            return

        try:
            em3 = discord.Embed(
                title=f"Du wurdest entmuted!",
                description=f'┌› 🔹〢 Moderator: {interaction.user.mention}\n'
                            f'├› 🔹〢 Moderator ID: `{interaction.user.id}`\n'
                            f'├› 🔹〢 In Guild: `{interaction.guild.name}`\n'
                            f'├› 🔹〢 User: {member.mention}\n'
                            f'├› 🔹〢 ID: `{member.id}`\n'
                            f'└› 🔹〢 Action: **Unmute**\n',
                color=0xee00e3
            )
            em3.set_footer(text="Bot Created by Ƒʉͫcͧкͭιͪηͣ dbxflame#4141")
            await member.send(embed=em3)
            return

        except:
            dmE = discord.Embed(
                title=f'Error',
                description=f'{member.mention} got __unmuted__ but I wasnt able to sent a DM Notification.',
                color=0xee00e3,
                timestamp=datetime.now()
            )
            await interaction.followup.send(embed=dmE, ephemeral=True)



def setup(client):
    client.add_cog(unmute(client))