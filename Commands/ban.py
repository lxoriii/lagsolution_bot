import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from datetime import datetime
import asyncio


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description='Banne einen User')
    @commands.has_role('➤╏Lag Solution')
    async def ban(
        self, 
        interaction: discord.Interaction, 
        member: Option(discord.Member, "Wähle einen user aus den du Banned willst"), 
        reason: Option(str, "Der Grund")
        ):

        await interaction.response.defer()
        await asyncio.sleep(0.5)

        try:
            emB = discord.Embed(
                title=f'Banned {member.name}!',
                description=f'┌› 🔹〢 Moderator: {interaction.user.mention}\n'
                            f'├› 🔹〢 Moderator ID: `{interaction.user.id}`\n'
                            f'├› 🔹〢 In Guild: `{interaction.guild.name}`\n'
                            f'├› 🔹〢 User: {member.mention}\n'
                            f'├› 🔹〢 ID: `{member.id}`\n'
                            f'├› 🔹〢 Aktion: **Banned**\n'
                            f'└› 🔹〢 Grund: **{reason}**',
                color=0xee00e3
            )
            await interaction.followup.send(embed=emB)

        except:
            em1 = discord.Embed(
            title=f'Error',
            description=f'Ich konnte {member.mention} nicht bannen. \n`MISSING_PERMISSION`',
            color=0xee00e3,
            timestamp=datetime.now()
            )

            await interaction.followup.send(embed=em1, ephemeral=True)
            return


        try:
            emDM = discord.Embed(
                title=f"Du wurdest gebannt!",
                description=f'┌› 🔹〢 Moderator: {interaction.user.mention}\n'
                            f'├› 🔹〢 Moderator ID: `{interaction.user.id}`\n'
                            f'├› 🔹〢 In Guild: `{interaction.guild.name}`\n'
                            f'├› 🔹〢 User: {member.mention}\n'
                            f'├› 🔹〢 ID: `{member.id}`\n'
                            f'├› 🔹〢 Aktion: **Banned**\n'
                            f'└› 🔹〢 Grund: **{reason}**',
                color=0xee00e3
            )
            await member.send(embed=emDM)
            await member.ban(reason=reason)

        except:
            dmE = discord.Embed(
                title=f'Error',
                description=f'{interaction.mention} wurde __gebannt__ aber ich konte keine DM notifikation schicken.',
                color=0xee00e3,
                timestamp=datetime.now()
            )
            await interaction.followup.send(embed=dmE, ephemeral=True)


def setup(client):
     client.add_cog(Ban(client))
