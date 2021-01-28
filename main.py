import os
import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("listo xd")

client.run(os.environ["BOT_TOKEN"])