import os
from random import *
import discord
from dotenv import load_dotenv
from discord.ext import commands
import re
# on importe tout le nécessaire


DISCORD_TOKEN={os.environ.get('token')}
DISCORD_GUILD={os.environ.get('guild')}
Cooldown = 0

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
    if message.author != client.user: #on vérifie que ce n'est pas un message du bot*
        if len(message.content) > 4 and message.content[1:3] == "an " and message.content.upper()[0] == 'P': #Quand le premier mot est la commande pan et suivi d'une cible
            print("PAN !")
            l = [", en plein dans le mille.", ", ça l'a touché.", ", headshot.", ", mais ça a raté.", ", mais il se tire dans le pied."] #Fin de phrase
            response = "<@" + str(message.author.id) + "> a tiré sur " + message.content[4:] + l[randint(0, len(l) - 1)]
            await message.channel.send(response)
        else:
            if "MILLION" in message.content.upper():
                print("MILLION")
                await message.channel.send("https://media1.tenor.com/images/e8fbc4408c8cbf27494788ee6ac08229/tenor.gif?itemid=24504749")
            if "D\'ACCORD" in message.content.upper():
                print("D\'ACCORD")
                await message.channel.send("https://tenor.com/view/asterix-vinalti-daccord-sure-ok-gif-15819283")
            if "DACCORD" in message.content.upper():
                print("DACCORD")
                await message.channel.send("https://tenor.com/view/asterix-vinalti-daccord-sure-ok-gif-15819283")
            if "QUOI" in message.content.upper():
                quoi=re.sub(r'[^a-zA-Z0-9]', '', message.content.upper())
                qlen = len(quoi)
                if (quoi[qlen-4] == "Q" and (quoi[qlen-3]) == "U" and (quoi[qlen-2]) == "O" and (quoi[qlen-1]) == "I"):
                    print("feur")
                    await message.channel.send("feur")
            if "BITE" in message.content.upper():
                print("BITE")
                bite = ["Bit", "Bite", "Shit", "Zizi", "Pipi", "Oui ?"] #Liste des réponses à bite
                await message.channel.send(bite[randint(0, len(bite) - 1)])
            if "ZIZI CACA" in message.content.upper(): #on vérifie que le bot à été ping
                liste=[]
                channel = discord.utils.get(client.get_all_channels(), guild__name='Le Bordel', name='chaine-de-mot') #on sélectionne le channel dans lequel on va prendre les messages
                async for texte in channel.history(limit=500):
                    if texte.author != client.user:
                        liste.append(texte.content) #on ajoute les messages à la liste
                print(liste)
                print(liste[randint(0,len(liste)-1)])
                response = liste[randint(0,len(liste)-1)] #on prend une réponse au hasard dans la liste
                await message.channel.send(response) #on répond
            if client.user.mentioned_in(message) and message.mention_everyone is False:
                maybe=randint(0,1)
                if maybe==0:
                    print("non")
                    await message.channel.send("non")
                else:
                    print("oui")
                    await message.channel.send("oui")
        if message.author.id == 505682488694145035 or message.author.id == 513429177433849867: #505682488694145035 id bbq, 513429177433849867 id youyou
            global Cooldown
            if (Cooldown == 0):
                bbq = 0
                youyou = 0
                async for msg in message.channel.history(limit=10):
                    if (msg.author.id == 505682488694145035):
                        bbq+=1
                    if (msg.author.id == 513429177433849867):
                        youyou+=1
                if (bbq >= 3 and youyou >= 3):
                    print("Vos gueules")
                    Cooldown = 50
                    await message.channel.send("https://tenor.com/view/jdg-harry-potter-albus-humblebundledor-humblebundledor-shut-up-gif-17560366")
            elif (Cooldown > 0):
                Cooldown -=1
client.run(os.environ.get('token'))
