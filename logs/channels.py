import disnake
from disnake.ext import commands
import os
import asyncio
import datetime
import config
import chi

intents = disnake.Intents.all()

class logRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_guild_role_delete(self, role:disnake.Role):
        guild = disnake.utils.get_guild(1095398284845137920)
        
        roleName = role.name
        roleId = role.id
        roleCol = role.color

        print(roleName)

def setup(bot):
    bot.add_cog(logRoles(bot))