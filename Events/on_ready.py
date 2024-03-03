import discord
from discord.ext  import commands
from discord.commands import slash_command
from datetime import datetime
import asyncio
from Views.TicketViews.CloseDropdownMenu import CloseDropdown
from Views.TicketViews.OrderMenu import OrderMenu
from Views.TicketViews.TicketButtonsEm import TicketViewButtonEmMSG
from Views.TicketView import TicketViewCreateTicket
from Views.VerifyView import VerifyView
from Views.VerifyViews.ButtonintoView import Buttonintomodal

class on_ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener(
        'on_ready'
    )
    async def listener(
        self
    ):
        self.client.add_view(
            TicketViewCreateTicket()
        )
        self.client.add_view(
            TicketViewButtonEmMSG()
        )
        self.client.add_view(
            CloseDropdown()
        )
        self.client.add_view(
            OrderMenu()
        )
        self.client.add_view(
            VerifyView()
        )
        self.client.add_view(
            Buttonintomodal()
        )


def setup(client):
     client.add_cog(on_ready(client))
