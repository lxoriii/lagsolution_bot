import discord
from discord.ext  import commands
from discord.commands import slash_command
from datetime import datetime
import asyncio
from Views.TicketView import TicketViewCreateTicket

class TicketMSG(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description='Owner Command only!')
    @commands.has_role('➤╏Geschäftsführung')
    async def ticketmsg(self, interaction):
        em = discord.Embed(
            title='Lag Solution',
            description=f'Ticket Regeln\n'
                        '> Unsinniges erstellen eines Tickets wird bestrafft\n'
                        '> Sei geduldig'
                        '> Pinge keine Teamler\n\n'

                        'Ticket Categories\n'
                        '**Support Ticket**\n'
                        '> ➥ Wenn du hilfe bei etwas brauchst, erstelle ein Support Ticket\n'

                        '**Bestellung**\n'
                        '> ➥ Kaufe etwas aus unserem Shops!\n'

                        '**Partner Anfrage**\n'
                        '> ➥ Hier kannst du eine Partner Anfrage einreichen \n'

                        '**Report**\n'
                        '> ➥ Reporte einen User/Glitch oder DDoS Angriff\n'

                        '**Bewerbung**\n'
                        '> ➥ Sei Teil unseres Teams',
            color=0x0b83f3
        )

        ticketmsg = self.client.get_channel(1045522690871668796)

        await ticketmsg.send(embed=em, view=TicketViewCreateTicket())
        await interaction.response.send_message('posted', ephemeral=True)

def setup(client):
     client.add_cog(TicketMSG(client))
