import discord
from discord.ext  import commands
from datetime import datetime
import asyncio
from Views.TicketViews.CloseDropdownMenu import CloseDropdown
import os


class TicketViewButtonEmMSG(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(
        label='Schließen',
        style=discord.ButtonStyle.red,
        custom_id='close'
    )
    async def callback1(self, button, interaction):

        emClose = discord.Embed(
            title='Ticket schließen',
            description=f'`┌›` Bitte gebe im Dropdown menu an, wieso Sie dieses Ticket schließen.\n'
                        f'`└›` Info: Dein @ wird in den Logs auftauchen.',
            color=0x2F3136
        )
        await interaction.response.send_message(embed=emClose, view=CloseDropdown(), ephemeral=True)


    @discord.ui.button(
        label='Übernehmen',
        style=discord.ButtonStyle.green,
        custom_id="ClaimTicket"
    )
    async def callback(self, button, interaction):
        member = interaction.user
        guild = interaction.guild
        staffRole = discord.utils.get(guild.roles, name='➤╏Lag Solution')
        
        if staffRole in member.roles:
            ClaimEm = discord.Embed(
                title='Ticket wurde geclaimed!',
                description=f'`┌›` Hallo, ich bin {member.mention} und habe __**dein Ticket übernommen**__\n'
                            f'`├›` Ich werde dir zur hilfe bereitstehen und deine Fragen __**beantworten**__\n'
                            f'`└›` Meine ID: {member.id}',
                color=0x2F3136,
                timestamp=datetime.now()
            )
            await interaction.response.send_message(embed=ClaimEm)
            button.disabled = True
            await interaction.message.edit(view=self)

        else:
            Err = discord.Embed(
                title=f'Error!',
                description=f'`›` Du kannst dein eigenes Ticket nicht übernehmen!',
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=Err, ephemeral=True)
