import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "dpy!")

@client.event
async def on_ready():
    print("listo xd")

client.run(os.getenv("BOT_TOKEN"))