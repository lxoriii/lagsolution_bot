import discord
import datetime
from datetime import datetime, timedelta
import random
import json
import os
import asyncio

custom_id = random.randint(1, 1000000)



class GiveawayModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label="Dauer",
                placeholder="z.B: 10m"
            ),
            discord.ui.InputText(
                label="Preis",
                placeholder="Der Preis den der User gewinnen soll.",
                style=discord.InputTextStyle.long
            ),
            discord.ui.InputText(
                label="Gewinner Anzahl",
                placeholder="Wie viele leute sollen Gewinnen?",
                style=discord.InputTextStyle.short
            ),
            discord.ui.InputText(
                label="Beschreibung",
                placeholder="Beschreibe dein Giveaway",
                style=discord.InputTextStyle.long,
                required=False,
            ),
            *args,
            **kwargs
        )

    async def callback(self, interaction):
        client = interaction.client

        if 's' in self.children[0].value:
            MDelta = self.children[0].value.replace('s', '')
            DeltaM = datetime.now() + timedelta(seconds=int(MDelta))
            time = discord.utils.format_dt(DeltaM, 'R')
            time2 = discord.utils.format_dt(DeltaM)
            timestamp = datetime.now() + timedelta(seconds=int(MDelta))
            asy = int(MDelta)

        elif 'm' in self.children[0].value:
            MDelta = self.children[0].value.replace('m', '')
            DeltaM = datetime.now() + timedelta(minutes=int(MDelta))
            time = discord.utils.format_dt(DeltaM, 'R')
            time2 = discord.utils.format_dt(DeltaM)
            timestamp = datetime.now() + timedelta(minutes=int(MDelta))
            asy = int(MDelta)*60

        elif 'h' in self.children[0].value:
            MDelta = self.children[0].value.replace('h', '')
            DeltaM = datetime.now() + timedelta(hours=int(MDelta))
            time = discord.utils.format_dt(DeltaM, 'R')
            time2 = discord.utils.format_dt(DeltaM)
            timestamp = datetime.now() + timedelta(hours=int(MDelta))
            asy = int(MDelta)*3600

        elif 'd' in self.children[0].value:
            MDelta = self.children[0].value.replace('d', '')
            DeltaM = datetime.now() + timedelta(days=int(MDelta))
            time = discord.utils.format_dt(DeltaM, 'R')
            time2 = discord.utils.format_dt(DeltaM)
            timestamp = datetime.now() + timedelta(days=int(MDelta))
            asy = int(MDelta)*3600*24


        embed = discord.Embed(
            title=f'🎉 `{self.children[1].value}` 🎉',
            description=f"""
{self.children[3].value}

× **{self.children[2].value}** Gewinner
× **Endet:** {time}  |  {time2}
× **Erstellt von:** {interaction.user.mention}
                        """,
            color=0xf7a1ff,
            timestamp=timestamp
        )
        embed.set_footer(text="Bot created by dbxflame")

        my_msg = await interaction.response.send_message(embed=embed, view=GiveawayEnter())

        giveaway = await my_msg.original_response()
        new_msg = client.get_message(giveaway.id)

        await asyncio.sleep(int(asy))

        winners_number = int(self.children[2].value)
        users = []


        with open(f"giveaway_users/{custom_id}.txt", "r") as file:
            for line in file:
                stripped_line = line.strip()
                users.append(stripped_line)

        winners = random.sample(users, int(winners_number))
        
        Winner = ''

        for w in winners:

            Winner += f'<@{w}>  '


        embed2 = discord.Embed(
            title=f'🎉 **|** Das Giveaway ist zu ende!',
            description=f"""
`Du bist zuspät :/`

**Preis:** 🎉 `{self.children[1].value}` 🎉

× **Gewinner:** {Winner}
× **Geendet:** {time}  |  {time2}
× **Erstellt von:** {interaction.user.mention}
                        """,
            color=0xf7a1ff,
            timestamp=timestamp
        )
        embed2.set_footer(text="Bot programmiert von FUTURISTC | dbxflame")


        await new_msg.edit(f'🎉 **|** {Winner} hat das Giveaway gewonnen', embed=embed2, view=None)
        os.remove(f"giveaway_users/{custom_id}.txt")



giveaway_users = []

class GiveawayEnter(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(
        label='Enter', custom_id=str(custom_id), style=discord.ButtonStyle.gray, emoji="🎉"
    )
    async def callback(self, button: discord.Button, interaction: discord.Interaction):
        member = interaction.user
        giveaway_users = []

        if os.path.exists(f"giveaway_users/{custom_id}.txt"):
            pass

        else:
            open(f"giveaway_users/{custom_id}.txt", "x")
            pass
        

        with open(f"giveaway_users/{custom_id}.txt", "r") as file:
            for line in file:
                stripped_line = line.strip()
                giveaway_users.append(stripped_line)


        if str(member.id) not in giveaway_users:
            await interaction.response.send_message("🎉 **|** Du bist **erfolgreich** dem **Giveaway** beigetreten!", ephemeral=True)
            a = member.id
            with open(f'giveaway_users/{custom_id}.txt', 'a') as file:
                file.write(f'{str(a)}\n')


        else:
            await interaction.response.send_message("🎉 **|** Du bist bist **bereits** dem Giveaway begetreten!", ephemeral=True)