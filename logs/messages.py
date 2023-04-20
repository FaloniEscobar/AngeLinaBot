import discord
from discord.ext import commands
import os
import asyncio
import datetime
import config
import chi

intents = discord.Intents.all()

class logMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, after, before):
        
        afterMsg = after.content
        beforeMsg = before.content
        userName = after.author.name + '#' + after.author.discriminator
        userID = after.author.id
        time = datetime.datetime.now()

        embed = discord.Embed(
            title = "Сообщение изменено",
            color = 0xff4545,
            timestamp = time
        )
        embed.add_field(
            name=f"До:",
            value=f"{afterMsg}",
            inline="True"
        )
        embed.add_field(
            name=f"После:",
            value=f"{beforeMsg}",
            inline="True"
        )
        embed.add_field(
            name=f"Пользователь:",
            value=f"{userName}",
            inline="False"
        )
        embed.add_field(
            name=f"ID:",
            value=f"{userID}",
            inline="True"
        )
        embed.set_footer(
            text=f"{config.bot_login}"
        )

        await self.bot.get_channel(chi.log_messages_id).send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        
        msg = message.content
        userName = message.author.name + '#' + message.author.discriminator
        userID = message.author.id
        time = datetime.datetime.now()

        embed = discord.Embed(
            title = "Сообщение удалено",
            color = 0xff4545,
            timestamp = time
        )
        embed.add_field(
            name=f"Сообщение:",
            value=f"{msg}",
            inline="True"
        )
        embed.add_field(
            name=f"Автор:",
            value=f"{userName}",
            inline="False"
        )
        embed.add_field(
            name=f"ID:",
            value=f"{userID}",
            inline="False"
        )
        embed.set_footer(
            text = f"{config.bot_login}"
        )

        await self.bot.get_channel(chi.log_messages_id).send(embed=embed)

def setup(bot):
    bot.add_cog(logMessages(bot))