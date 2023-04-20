import asyncio
import disnake
from disnake.ext import commands
import os

import config as config
token = config.key
prefix = config.bot_prefix

bot = commands.Bot(intents=disnake.Intents.all(), command_prefix=prefix, test_guilds=[1095398284845137920], help_command=None)
# intents.message_content = True

@bot.event
async def on_ready():
    print('Active!')

for file in os.listdir("./head"):
    if file.endswith(".py"):
        try:
            bot.load_extension(f"head.{file[:-3]}")
        except Exception as e: print(f"Error: {e}")

for file in os.listdir("./logs"):
    if file.endswith(".py"):
        try:
            bot.load_extension(f"logs.{file[:-3]}")
        except Exception as e: print(f"Error: {e}")

bot.run(str(token))