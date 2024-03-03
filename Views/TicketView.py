import discord
from discord.ext  import commands
from datetime import datetime
import asyncio
from Views.TicketViews.TicketButtonsEm import TicketViewButtonEmMSG
from Views.TicketViews.OrderMenu import OrderMenu
from Views.TicketViews.ReportDropDown import Rep
from Views.TicketViews.applicationDropdown import appdropdown
from Views.TicketViews.PartnerModal import PartnerModal


TicketOptionss = [
    discord.SelectOption(label="Support", description="Support-Ticket: For general Support", emoji="<:DBX:1047486135930200084>", value="support"),
    discord.SelectOption(label="Bestellung", description="Order-Ticket: Kaufe etwas aus unserem Shop", emoji="<:DBXdolla:1047486144155222096>", value="order"),
    discord.SelectOption(label="Partnerschaft", description="Partnerschaft-Ticket: Partneranfrage? Klicke hier!", emoji="<:DBXPartner:1047562037590499379>", value="partner"),
    discord.SelectOption(label="Report", description="Report-Ticket: Reporte einen User/Glitch/DDoS Angriff", emoji="<:DBXtos:1047271034795081778>", value="report"),
    discord.SelectOption(label="Bewerbung", description="Bewerbung-Ticket: Sei ein Teil unseres Teams!", emoji="<:DBXguide:1047271036112089088>", value="app")
]

class TicketViewCreateTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Select a Topic",
        options=TicketOptionss,
        custom_id="CreateTickett"
    )
    async def select_callback(self, select, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild

        if 'support' in select.values:
            cat = client.get_channel(1045587107948802049)
            ticket_channel = await interaction.guild.create_text_channel(
                f'ticket-{interaction.user}',
                topic=f'Ticket von {interaction.user}\nClient-ID: {interaction.user.id}',
                category=cat
            )

            try:
                embed1 = discord.Embed(
                    description=f'Ticket wird erstellt...',
                    color=discord.Color.green()
                )
                t = await interaction.response.send_message(embed=embed1, ephemeral=True)

                msg = await t.original_response()

                await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, view_channel=True)
                await ticket_channel.set_permissions(interaction.guild.get_role(1045522636341510235), send_messages=True, read_messages=True, view_channel=True)
                await ticket_channel.set_permissions(interaction.guild.default_role, view_channel=False)

                embed2 = discord.Embed(
                    title='📬 Ticket wurde erstellt!',
                    description=f'`┌›` Dein Ticket: {ticket_channel.mention}\n'
                                f'`└›` Ticket Besitzer: {member.mention}',
                    color=0x0b83f3,
                    timestamp=datetime.now()
                )
                await interaction.followup.edit_message(embed=embed2, message_id=msg.id)

            except:
                em1E = discord.Embed(
                    title='📬 Error!',
                    description=f'{member.mention}, Ich hatte probleme beim erstellen deines Tickets, bitte reporte das einem Developer / Owner so schnell wie möglich !',
                    color=discord.Color.red(),
                    timestamp=datetime.now()
                )
                await interaction.response.send_message(embed=em1E, ephemeral=True)
                return

            embed3 = discord.Embed(
                title=f'Ticket-{member.name}',
                description=f'Hier ist dein Ticket, {member.mention}\n'
                            f'Zu beginn, fülle bitte folgende fragen aus:\n'
                            f'`┌›` Wieso hast du dieses Ticket erstellt?\n'
                            f'`├›` Gibt es (falls nötig) beweise dafür?\n'
                            f'`└›` Bitte sei geduldig und warte auf ein Teamler.',
                color=0x0b83f3,
                timestamp=datetime.now()
            )
            embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/1051979242591752202/1051993707991289896/website-removebg-preview.png')
            await ticket_channel.send('<@&1045522636341510235>', embed=embed3, view=TicketViewButtonEmMSG())



        if 'order' in select.values:
            em2 = discord.Embed(
                title='Bestellung',
                description=f'Was möchtest du gerne bestellen?\nBitte wähle dies aus im folgendem Dropdown Menu.',
                color=0x2F3136,
                timestamp=datetime.now()
            )
            await interaction.response.send_message(embed=em2, view=OrderMenu(), ephemeral=True)



        if 'partner' in select.values:

            await interaction.response.send_modal(PartnerModal(title='Partner Anfrage'))



        if 'report' in select.values:
            em2 = discord.Embed(
                title='Report',
                description=f'Was würdest du gerne reporten?\nnBitte wähle dies aus im folgendem Dropdown Menu.',
                color=0x2F3136,
                timestamp=datetime.now()
            )
            await interaction.response.send_message(embed=em2, view=Rep(), ephemeral=True)


        if 'app' in select.values:
            em2 = discord.Embed(
                title='Bewerbung',
                description=f'Als was möchtest du dich gerne Bewerben?\nBitte wähle dies aus im folgendem Dropdown Menu.',
                color=0x2F3136,
                timestamp=datetime.now()
            )
            await interaction.response.send_message(embed=em2, view=appdropdown(), ephemeral=True)