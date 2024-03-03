import discord


class EmbedSetup(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label="Channel ID",
                placeholder="Die ID vom Channel wo der Embed hin geschickt werden soll",
                style=discord.InputTextStyle.short,
            ),
            discord.ui.InputText(
                label="Embed Title",
                placeholder="Title"
            ),
            discord.ui.InputText(
                label="Embed Description",
                placeholder="Description",
                style=discord.InputTextStyle.long
            ),
            discord.ui.InputText(
                label="Embed Field 1",
                placeholder="Field 1",
                style=discord.InputTextStyle.long,
                required=False,
            ),
            discord.ui.InputText(
                label="Embed Field 2",
                placeholder="Field 2",
                style=discord.InputTextStyle.long,
                required=False,
            ),
            *args,
            **kwargs
        )

    async def callback(self, interaction):
        client = interaction.client
        channel = client.get_channel(int(self.children[0].value))

        embed = discord.Embed(
            title=self.children[1].value,
            description=f'{self.children[2].value}\n\n{self.children[3].value}\n\n{self.children[4].value}',
            color=0x3398ee
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1063594036117647452/1063594249217646685/Comp_104.gif')
        embed.set_footer(icon_url='https://cdn.discordapp.com/attachments/1063594036117647452/1063594249217646685/Comp_104.gif', text='Made with ❤️')
        await channel.send(embed=embed)
        await interaction.response.send_message('Embed geschickt!', ephemeral=True)
