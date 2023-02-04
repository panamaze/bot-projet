import discord
import random
from discord.ext import commands

client = discord.Client(command_prefix='!')
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Je suis connécté")

@client.command()
async def commandes(ctx):
    embed = discord.Embed(
        title="Liste des commandes disponibles",
        description="Voici les commandes que je peux faire:",
        color=discord.Color.blue()
    )
    embed.add_field(name="!commandes", value="Montre toute les commandes du bot", inline=False)
    embed.add_field(name="!ping", value="Affiche la latence du bot", inline=False)
    embed.add_field(name="!avatar", value="Affiche l'avatar de la personne mentionnée", inline=False)
    embed.add_field(name="!ticket create", value="Crée un salon ticket avec un nom aléatoire", inline=False)
    embed.add_field(name="!ticket delete", value="Supprime le salon ticket actuel", inline=False)
    embed.add_field(name="!mute", value="Met le role `mute` à la personne mentionnée", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f"Latence: {round(client.latency * 1000)}ms")


@client.event
async def on_message(message):
    if "http" in message.content:
        await message.delete()
        await message.channel.send("Les liens sont interdits dans le chat.")

@client.command()
async def avatar(ctx, member: discord.Member):
    embed = discord.Embed(
    title=f"Avatar de {member}",
    color=discord.Color.blue()
    )
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def ticket_create(ctx):
    channel = await ctx.guild.create_text_channel(f"ticket-{random.randint(1, 100)}")
    await channel.send("Ceci est un salon ticket.")

@client.command()
async def ticket_delete(ctx):
    if ctx.channel.name.startswith("ticket-"):
        await ctx.channel.delete()
    else:
        await ctx.send("Ce salon n'est pas un salon ticket.")


@client.command()
async def mute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.guild.roles, name="mute")
    if mute_role is None:
        await ctx.send("Le role `mute` n'existe pas sur ce serveur")
        return
    await member.add_roles(mute_role)
    await ctx.send(f"{member.mention} a été rendu muet.")
    
client.run("tkt pas")
