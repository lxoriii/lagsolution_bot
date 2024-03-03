import discord
from datetime import datetime
from discord.ext import commands, tasks
import asyncio

class onMemberJoin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        guild = member.guild
        for channel in member.guild.channels:
            if channel.name.startswith('🔮│Member -'):
                await channel.edit(name=f'🔮│Member - {member.guild.member_count}')  
        Welcome = self.client.get_channel(1045522664393023508)

        a = guild.get_role(1073077745275383949)
        e = guild.get_role(1073072828129222726)
        f = guild.get_role(1073077256668323890)
        g = guild.get_role(1073077100682166333)

        WelcomeEmbed = discord.Embed(
            title=f"Willkommen !",
            description=f"`>` {member.mention}\n**Danke das du joinst !**\n**Verifiziere dich und lese unsere Regeln.**\n**Du hast fragen? Frag uns!**\n\n**Viel glück und viel spaß!**",
            color=0x0b83f3,
            timestamp=datetime.now()
        )
        WelcomeEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1051979242591752202/1051993707991289896/website-removebg-preview.png")
        WelcomeEmbed.set_footer(text="Lag Solution | Next Gen Hosting")
        await Welcome.send(embed=WelcomeEmbed)
        await member.add_roles(a,e,f,g)

        if member.guild.members == 500:
            stop = []
            if stop == None:
                c = self.client.get_channel(1045522697104408677)

                await c.send('<@622126000720969751> <@1051237539488477244> es sind jzt 500 member auf lag solution du kek.')

            else:
                return



def setup(client):
     client.add_cog(onMemberJoin(client))