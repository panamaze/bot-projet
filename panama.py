import discord
import random

def check_role(author):
    if "bot" not in [role.name for role in author.roles]:
        return False
    return True

client = discord.Client()

@client.event
async def on_ready():
    print("Je suis online")

@client.event
async def on_message(message):
    if message.content.startswith("!ping"):
        await message.channel.send(f"Latence: {round(client.latency * 1000)}ms")

@client.event
async def on_message(message):
    if message.content.startswith("!ping"):
        await message.channel.send(f"Latence: {round(client.latency * 1000)}ms")

    if message.content.startswith("!help"):
        embed = discord.Embed(
            title="Liste des commandes disponibles",
            description="Voici les commandes que je peux faire:",
            color=discord.Color.blue()
        )

        embed.add_field(name="!ping", value="Affiche la latence du bot", inline=False)
        embed.add_field(name="!avatar", value="Affiche l'avatar de la personne mentionnée", inline=False)
        embed.add_field(name="!ticket create", value="Crée un salon ticket avec un nom aléatoire", inline=False)
        embed.add_field(name="!ticket delete", value="Supprime le salon ticket actuel", inline=False)

        await message.channel.send(embed=embed)


    if message.content.startswith("http"):
        await message.delete()
        await message.channel.send("Les liens sont interdits dans le chat.")

    if message.content.startswith("!avatar"):
        user = message.mentions[0]
        embed = discord.Embed(
            title=f"Avatar de {user}",
            color=discord.Color.blue()
        )
        embed.set_image(url=user.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("!ticket create"):
        if check_role(message.author):
            channel = await message.guild.create_text_channel(f"ticket-{random.randint(1, 100)}")
        await channel.send("Ceci est un salon ticket.")

    if message.content.startswith("!ticket delete"):
        if check_role(message.author):
            if message.channel.name.startswith("ticket-"):
                await message.channel.delete()
        else:
            await message.channel.send("Ce salon n'est pas un salon ticket.")

client.run("tkt pas")
