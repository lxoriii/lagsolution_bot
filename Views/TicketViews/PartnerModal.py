import discord
from datetime import datetime
from Views.TicketViews.TicketButtonsEm import TicketViewButtonEmMSG

class PartnerModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label="Wie viele Member hast du?",
                placeholder="Wie viele Member hast du?",
                style=discord.InputTextStyle.short
            ),
            discord.ui.InputText(
                label="Was für einen Nutzen haben wir?",
                placeholder="...",
                style=discord.InputTextStyle.long
            ),
            discord.ui.InputText(
                label="Ist dein Server aktiv?",
                placeholder="ja/nein",
                style=discord.InputTextStyle.long,
            ),
            *args,
            **kwargs
        )

    async def callback(self, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild

        cat = client.get_channel(1049066866099884142)
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
                description=f'{member.mention}, Ich hatte probleme beim erstellen Ihres Tickets ! Bitte Reporte das so schnell wie möglich einem Teamler',
                color=discord.Color.red(),
                timestamp=datetime.now()
            )
            await interaction.response.send_message(embed=em1E, ephemeral=True)
            return

        embed3 = discord.Embed(
            title=f'Ticket-{member.name}',
            description=f'Hier ist dein Ticket, {member.mention}\n'
                        f'`┌›` Aktuelle Member Anzahl: `{self.children[0].value}`\n'
                        f'`├›` Was für einen Nutzen haben wir durch eine Partnerschaft?: `{self.children[1].value}`\n'
                        f'`├›` Ist dein Server aktiv?: `{self.children[2].value}`\n'
                        f'`└›` Bitte sei geduldig und warte auf einen Teamler.',
            color=0x0b83f3,
            timestamp=datetime.now()
        )
        embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/1051979242591752202/1051993707991289896/website-removebg-preview.png')
        await ticket_channel.send('<@&1045522636341510235>', embed=embed3, view=TicketViewButtonEmMSG())
