import discord
from discord.ext  import commands
from discord.commands import slash_command
from datetime import datetime
import asyncio
from Views.VerifyView import VerifyView

class verifymsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description='Owner Command only!')
    @commands.has_role('➤╏Geschäftsführung')
    async def verifymsg(self, interaction):
        em = discord.Embed(
            title='Lag Solution',
            description=f'Verifikation\n'
                        '**Wie kann ich mich verifizieren?**\n'
                        '> ➥ Klicke auf das select Menu und\n'
                        '> ➥ klick/fülle das richtige aus.\n\n'

                        'Was soll ich tun wenn das nicht funktioniert?\n'
                        '> ➥ DM dbxFlame und frage ihn nach Hilfe.\n'
                        '> ➥ Er wird schnellstmöglich antworten!',
            color=0x0b83f3
        )

        verifymsg = self.client.get_channel(1052526476450344990)

        await verifymsg.send(embed=em, view=VerifyView())
        await interaction.response.send_message('posted', ephemeral=True)

def setup(client):
     client.add_cog(verifymsg(client))
