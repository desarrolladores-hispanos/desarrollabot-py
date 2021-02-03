import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "dpy!")

@client.event
async def on_ready():
    await client.change_presence(
        activity = discord.Activity(
            type = discord.ActivityType.listening,
            name = "corridones"
        )
    )

@client.command()
async def pato(ctx):
	new_embed = discord.Embed(
		title = "Un pato",
		description = f"Cuá cuá, {ctx.message.author.mention}, ¡aquí está tu pato!",
		colour = discord.Colour.blue()
	)

	new_embed.set_author(name = "DesarrollaBot.py")
	new_embed.set_image(url = "https://www.random-d.uk/api/randomimg")
	await ctx.send(embed = new_embed)

@client.command()
@commands.has_permissions(administrator = True)
async def repetir(ctx, message):
	await ctx.message.delete()
	await ctx.send(message)

@client.command()
async def redes(ctx):
    await ctx.send(
        """
Twitter: <https://twitter.com/dh_rblx>
Sitio web: <https://desarrolladoreshispanos.com>
GitHub: <https://github.com/Desarrolladores-Hispanos>
Grupo de Roblox: <https://www.roblox.com/groups/9369198/Desarrolladores-Hispanos>
Discord: pues ya estás en el servidor xd
        """
    )

@client.command()
@commands.has_permissions(manage_messages = True)
async def eliminar(ctx, cantidad):
    await ctx.channel.purge(limit = int(cantidad) + 1)

@client.command()
async def convertir_a_robux(ctx, usd):
    await ctx.send("USD %.2f son <:robux:806422545359306752> %.2f" % (usd, usd/0.0035))

@client.command()
async def convertir_a_usd(ctx, robux):
    await ctx.send(f"<:robux:806422545359306752> %.2f son USD $%.2f" % (robux, robux*0.0035))

client.run(os.getenv("BOT_TOKEN"))