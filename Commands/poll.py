import discord
from datetime import datetime
from discord.ext import commands, tasks
from colorama import Fore
from discord.commands import slash_command, Option


class poll(commands.Cog):

    def __init__(self, client):
        self.client = client


    @slash_command(description='Erstelle eine Abstimmung')
    @commands.has_role('➤╏Lag Solution')
    async def abstimmung(self, ctx, *, message: Option(str), choice1: Option(str), choice2: Option(str), choice3: Option(str, required=False), choice4: Option(str, required=False)):
        
        await ctx.respond('Abstimmung wurde erfolgreich erstellt!', ephemeral=True)

        embed = discord.Embed(
            title=" ABSTIMMUNG ",
            description=f"{message}\n\n1️⃣\n {choice1}\n\n2️⃣\n {choice2}",
            color = discord.Color.blue()
        )

        if choice3 is not None:
            embed.add_field(name='3️⃣', value=f'{choice3}')

        if choice4 is not None:
            embed.add_field(name='4️⃣', value=f'{choice4}')

    
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")


        if choice3 is not None:
            await msg.add_reaction("3️⃣")

        if choice4 is not None:
            await msg.add_reaction("4️⃣")


def setup(client):
    client.add_cog(poll(client))