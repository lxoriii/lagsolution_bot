import discord
from datetime import datetime
from Views.TicketViews.TicketButtonsEm import TicketViewButtonEmMSG

options = [
    discord.SelectOption(label="Bewerbe dich als Moderator", description="Wenn du dich als Moderator Bewerben willst, klicke heir!", value="mod"),
    discord.SelectOption(label="Bewerbe dich als Developer", description="Wenn du dich als Developer Bewerben willst, klicke heir!", value="dev"),
    discord.SelectOption(label="Bewerbe dich als Partner Manager", description="Wenn du dich als Partner Manager Bewerben willst, klicke heir!", value="part")
]


class appdropdown(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Als was möchtest du dich Bewerben?",
        options=options,
        custom_id="appdrop"
    )
    async def select_callback(self, select, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild

        if "mod" in select.values:

            cat = client.get_channel(1047851117775691776)
            ticket_channel = await interaction.guild.create_text_channel(
                f'Mod-ticket-{interaction.user}',
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
                            f'`┌›` Bewerbungs Typ: `Moderator`\n'
                            f'`└›` Bitte sei geduldig und warte auf ein Teamler.',
                color=0x0b83f3,
                timestamp=datetime.now()
            )
            embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/1051979242591752202/1051993707991289896/website-removebg-preview.png')
            await ticket_channel.send('<@&1045522636341510235>', embed=embed3, view=TicketViewButtonEmMSG())


        if "dev" in select.values:

            cat = client.get_channel(1047851117775691776)
            ticket_channel = await interaction.guild.create_text_channel(
                f'Mod-ticket-{interaction.user}',
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
                            f'`┌›` Bewerbungs Typ: `Developer`\n'
                            f'`└›` Bitte sei geduldig und warte auf ein Teamler.',
                color=0x0b83f3,
                timestamp=datetime.now()
            )
            embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/1051979242591752202/1051993707991289896/website-removebg-preview.png')
            await ticket_channel.send('<@&1045522636341510235>', embed=embed3, view=TicketViewButtonEmMSG())


        if "part" in select.values:

            cat = client.get_channel(1047851117775691776)
            ticket_channel = await interaction.guild.create_text_channel(
                f'Mod-ticket-{interaction.user}',
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
                            f'`┌›` Bewerbungs Typ: `Partner Manager`\n'
                            f'`└›` Bitte sei geduldig und warte auf ein Teamler.',
                color=0x0b83f3,
                timestamp=datetime.now()
            )
            embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/1051979242591752202/1051993707991289896/website-removebg-preview.png')
            await ticket_channel.send('<@&1045522636341510235>', embed=embed3, view=TicketViewButtonEmMSG())