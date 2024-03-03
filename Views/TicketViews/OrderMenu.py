import discord
from discord.ext  import commands
from datetime import datetime
import asyncio
from Views.TicketViews.TicketButtonsEm import TicketViewButtonEmMSG

options = [
    discord.SelectOption(label="Dedicated Server", value="dedi"),
    discord.SelectOption(label="Website und Domain", value="website"),
    discord.SelectOption(label="Development Package", value="dev"),
    discord.SelectOption(label="Discord & TeamSpeak Bots", value="bot"),
    discord.SelectOption(label="TeamSpeak", value="ts")
]


class OrderMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Wähle eine Bestellung aus",
        options=options,
        custom_id="OrderMenu"
    )
    async def select_callback(self, select, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild

        if "dedi" in select.values:

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
                            f'`┌›` Bestellungs Typ: `Dedicated Server`\n'
                            f'`└›` Bitte sei geduldig und warte auf einen Teamler.',
                color=0x0b83f3,
                timestamp=datetime.now()
            )
            embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/1051979242591752202/1051993707991289896/website-removebg-preview.png')
            await ticket_channel.send('<@&1045522636341510235>', embed=embed3, view=TicketViewButtonEmMSG())



        if "website" in select.values:

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
                            f'`┌›` Bestellungs Typ: `Website & Domain`\n'
                            f'`└›` Bitte sei geduldig und warte auf einen Teamler.',
                color=0x0b83f3,
                timestamp=datetime.now()
            )
            embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/1047258923104735252/1047874309248528484/Dbx.png')
            await ticket_channel.send('<@&1045522636341510235>', embed=embed3, view=TicketViewButtonEmMSG())



        if "dev" in select.values:

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
                            f'`┌›` Bestellungs Typ: `Development Package`\n'
                            f'`└›` Bitte sei geduldig und warte auf einen Teamler.',
                color=0x0b83f3,
                timestamp=datetime.now()
            )
            embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/1047258923104735252/1047874309248528484/Dbx.png')
            await ticket_channel.send('<@&1045522636341510235>', embed=embed3, view=TicketViewButtonEmMSG())



        if "bot" in select.values:

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
                            f'`┌›` Bestellungs Typ: `Discord & TS Bots`\n'
                            f'`└›` Bitte sei geduldig und warte auf einen Teamler.',
                color=0x0b83f3,
                timestamp=datetime.now()
            )
            embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/1047258923104735252/1047874309248528484/Dbx.png')
            await ticket_channel.send('<@&1045522636341510235>', embed=embed3, view=TicketViewButtonEmMSG())




        if "ts" in select.values:

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
                            f'`┌›` Bestellungs Typ: `TeamSpeak`\n'
                            f'`└›` Bitte sei geduldig und warte auf einen Teamler.',
                color=0x0b83f3,
                timestamp=datetime.now()
            )
            embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/1047258923104735252/1047874309248528484/Dbx.png')
            await ticket_channel.send('<@&1045522636341510235>', embed=embed3, view=TicketViewButtonEmMSG())
