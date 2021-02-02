import os
import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = "dpy!")

@client.event
async def on_ready():
    print("listo xd")

@client.command()
async def pato(ctx):
	duck_number = randint(1, 138)
	url = f"https://www.random-d.uk/api/{duck_number}.jpg"
	new_embed = discord.Embed(
		title = f"Pato n°{duck_number}",
		description = f"Cuá cuá, {ctx.message.author.mention}, ¡aquí está tu pato!",
		colour = discord.Colour.blue()
	)

	new_embed.set_author(name = "DesarrollaBot.py")
	new_embed.set_image(url = url)
	await ctx.send(embed = new_embed)

client.run(os.getenv("BOT_TOKEN"))