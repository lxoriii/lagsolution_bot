import discord
from datetime import datetime
import asyncio
import os

class Logger:
    def __init__(
        self,
        channel: discord.TextChannel
    ):
        self.channel = channel

    async def create_log_file(
        self
    ):
        with open(f"Log {self.channel.name}.txt", "w", encoding="utf-8") as f:
            f.write(f'Log of the Ticket "{self.channel.name}"\n')
            f.write("########## START OF THE LOG ##########\n")
            messages = await self.channel.history(limit=69420).flatten()
            for i in reversed(messages):
                f.write(f"{i.created_at}: {i.author}: {i.content}\n")
            f.write("########## END OF THE LOG ##########\n\n")
            if len(messages) >= 69420:
                f.write(
                    f"More than 69420 messages got sent into that channel. Because of Save reasons,"
                    f"only the last 69420 messages got logged.")
            else:
                f.write(f"Message count: {len(messages)}")

    async def send_log_file(
        self,
        channel: discord.TextChannel
    ):
        await channel.send(
            files=[discord.File(f"Log {self.channel.name}.txt", filename=f"{self.channel.name}.txt")]
        )
        os.remove(
            f"Log {self.channel.name}.txt"
        )

class CloseModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label="Wieso schliest du dieses Ticket?",
                placeholder="Der Grund?",
                style=discord.InputTextStyle.short
            ),
            *args,
            **kwargs
        )

    async def callback(self, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild
        log = client.get_channel(1045522699696472134)

        em2 = discord.Embed(
            title='Ticket wird geschlossen...',
            description=f'3 Sekunden bis dieses Ticket geschlossen wird.',
            color=0x2F3136,
            timestamp=datetime.now()
        )
        await interaction.response.send_message(embed=em2)
        await asyncio.sleep(3)

        modchannel = client.get_channel(1045522699696472134)
        logger = Logger(interaction.channel)
        await logger.create_log_file()
        await logger.send_log_file(modchannel)

        await interaction.channel.delete()

        logg = discord.Embed(
            title='Ticket wurde geschlossen!',
            description=f'`┌›` Ticket: `{interaction.channel.name}`\n'
                        f'`├›` Geschlossen von: {member.mention}\n'
                        f'`└›` Grund: {self.children[0].value}',
            color=discord.Color.red(),
            timestamp=datetime.now()
        )
        await log.send(embed=logg)