import os
from random import *
import discord
from dotenv import load_dotenv
from discord.ext import commands
import re
from tokenfile import TOKEN
# on importe tout le nécessaire


DISCORD_TOKEN={"Njg5NDI5Njk2MDkzMzU2MDU0.XnCwRg.l5SwJ4C09rPZyNbBJpT6CQnyeUg"}
DISCORD_GUILD={"402063004998565910"}


load_dotenv()
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

 # on lance le bot


@client.event
async def on_message(message): #quand un message est envoyé 
    if message.author != client.user: #on vérifie que ce n'est pas un message du bot
        if "<@!689429696093356054>" in message.content.split(): #on vérifie que le bot à été ping
            liste=[]
            channel = discord.utils.get(client.get_all_channels(), guild__name='Ché Mwa', name='message') #on sélectionne le channel dans lequel on va prendre les messages
            async for texte in channel.history(limit=20):
                if texte.author != client.user:
                    liste.append(texte.content) #on ajoute les messages à la liste
            print(liste)
            print(liste[randint(0,len(liste)-1)])
            response = liste[randint(0,len(liste)-1)] #on prend une réponse au hasard dans la liste
            await message.channel.send(response) #on répond
client.run("Njg5NDI5Njk2MDkzMzU2MDU0.XnCwRg.l5SwJ4C09rPZyNbBJpT6CQnyeUg")
