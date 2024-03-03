import discord
from datetime import datetime
import asyncio
import random


class verifyModal(discord.ui.Modal):

    def __init__(self, *args, **kwargs):
        self.captcha_text = random.randint(100000, 999999)
        super().__init__(
            discord.ui.InputText(
                label=f"Code: {self.captcha_text}",
                placeholder=f"Schreibe hier den Code: | {self.captcha_text} |",
                style=discord.InputTextStyle.short
            ),
            *args,
            **kwargs
        )

    async def callback(self, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild

        if int(self.children[0].value) == self.captcha_text:
            role = discord.utils.get(guild.roles, name='➤╏Verified')
            await interaction.response.send_message('Du hast die verifikation mit erfolg bestanden!', ephemeral=True)
            await member.add_roles(role)

        else:
            emW = discord.Embed(
                title='Das ist falsch!',
                description=f'Bitte versuche es erneut!',
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=emW, ephemeral=True)
            return