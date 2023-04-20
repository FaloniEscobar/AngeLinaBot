import discord
from discord.ext import commands
import os
import asyncio
import datetime
import config
import chi

intents = discord.Intents.all()

class logUsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.member):
        
        userLogin = member
        userId = member.id
        userAvatar = str(member.display_avatar.url)
        time = datetime.datetime.now()

        embed = discord.Embed(
            title = f"Пользователь присоединился",
            color = 0x47ff4e,
            timestamp = time
        )
        embed.add_field(
            name=f"Пользователь:",
            value=f"{userLogin}"
        )
        embed.add_field(
            name=f"ID:",
            value=f"{userId}"
        )
        embed.set_thumbnail(
            url = userAvatar
        )
        embed.set_footer(
            text = f"{config.bot_login}"
        )

        await self.bot.get_channel(chi.log_players_id).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member:discord.member):      # пользователь вышел
        
        userLogin = member
        userId = member.id
        userAvatar = str(member.display_avatar.url)
        time = datetime.datetime.now()

        embed = discord.Embed(
            title = f"Пользователь отключился",
            color = 0xff4545,
            timestamp = time
        )
        embed.add_field(
            name=f"Пользователь:",
            value=f"{userLogin}"
        )
        embed.add_field(
            name=f"ID:",
            value=f"{userId}"
        )
        embed.set_thumbnail(
            url = userAvatar
        )
        embed.set_footer(
            text = f"{config.bot_login}"
        )

        await self.bot.get_channel(chi.log_players_id).send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):      # пользователь изменил ник
        

        userLogin = before
        userId = before.id

        nickBefore = before.nick       # до
        nickAfter = after.nick       # после

        userAvatar = str(before.display_avatar.url)
        time = datetime.datetime.now()

        embed = discord.Embed(
            title = f"Ник пользователя изменён",
            color = 0xff4545,
            timestamp = time
        )
        embed.add_field(
            name=f"До:",
            value=f"{nickBefore}",
            inline="True"
        )
        embed.add_field(
            name=f"После:",
            value=f"{nickAfter}",
            inline="True"
        )
        embed.add_field(
            name=f"Пользователь:",
            value=f"{userLogin}",
            inline="False"
        )
        embed.add_field(
            name=f"ID:",
            value=f"{userId}",
            inline="True"
        )
        embed.set_thumbnail(
            url = userAvatar
        )
        embed.set_footer(
            text = f"{config.bot_login}"
        )

        await self.bot.get_channel(chi.log_players_id).send(embed=embed)

def setup(bot):
    bot.add_cog(logUsers(bot))