import discord
from discord.ext  import commands
from datetime import datetime
import asyncio
from Views.VerifyViews.ButtonintoView import Buttonintomodal

Verification = [
    discord.SelectOption(label="Falsch", description="Das ist Falsch", emoji="<:DBXcross:1047486128653078568>", value="Falsch"),
    discord.SelectOption(label="richtig", description="Klicke hier um dich zu verifizieren", emoji="<:DBXtick:1047486130066567188>", value="richtig"),
    discord.SelectOption(label="Falsch", description="Das ist Falsch", emoji="<:DBXcross:1047486128653078568>", value="Falsch1"),
    discord.SelectOption(label="Falsch", description="Das ist Falsch", emoji="<:DBXcross:1047486128653078568>", value="Falsch2"),
    discord.SelectOption(label="Falsch", description="Das ist Falsch", emoji="<:DBXcross:1047486128653078568>", value="Falsch3"),
    discord.SelectOption(label="Falsch", description="Das ist Falsch", emoji="<:DBXcross:1047486128653078568>", value="Falsch4")
]

class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Klicke auf richtig",
        options=Verification,
        custom_id="StartVerification"
    )
    async def select_callback(self, select, interaction):

        if 'Falsch' in select.values or 'Falsch1' in select.values or 'Falsch2' in select.values or 'Falsch3' in select.values or 'Falsch4' in select.values:
            emW = discord.Embed(
                title='Das ist Falsch!',
                description=f'Bitte versuche es erneut!',
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=emW, ephemeral=True)
            return


        elif 'richtig' in select.values:
            emR = discord.Embed(
                title='Das ist korrekt!',
                description=f'Jezt nächster Schritt. Klicke auf den Button `Nächster Schritt` um fortzufahren.',
                color=discord.Color.green()
            )
            await interaction.response.send_message(embed=emR, view=Buttonintomodal(), ephemeral=True)
