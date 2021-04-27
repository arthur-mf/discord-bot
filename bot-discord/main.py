import discord
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print("le bot est pret")
@client.event
async def on_member_join(member):
    gen_channel: discord.TextChannel = client.get_channel(835848689112055810)
    await gen_channel.send(content=f"Bienvenue sur le serveur{member.display_name} !")

@client.event
async def on_message(message):
    if message.content.lower() == ".gen nitro":
       await message.channel.send ("Nitro généré! Verifie tes MP")

client.run(os.getenv("TOKEN"))