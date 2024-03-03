import discord
from discord.ext  import commands
from datetime import datetime
import asyncio
from Views.TicketViews.ReportModal import ReportUserModal, ReportGlitchModal, ReportddosModal


options = [
    discord.SelectOption(label="Reporte ein Glitch", description="Wenn du einen Glitch reporten willst, klicke hier!", value="glitch"),
    discord.SelectOption(label="Reporte einen User", description="Wenn du einen User reporten willst, klicke hier!", value="user"),
    discord.SelectOption(label="Reporte einen DDoS Angriff", description="Wenn dein Panel gedoss'd wird, klicke hier!", value="ddos")
]


class Rep(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Wähle die Art des Reportes",
        options=options,
        custom_id="rep"
    )
    async def select_callback(self, select, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild
        if "glitch" in select.values:

            await interaction.response.send_modal(ReportGlitchModal(title='Glitch report'))


        if "user" in select.values:

            await interaction.response.send_modal(ReportUserModal(title='User report'))


        if "ddos" in select.values:

            await interaction.response.send_modal(ReportddosModal(title='DDoS report'))