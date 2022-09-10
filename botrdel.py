import os
from random import *
import discord
from dotenv import load_dotenv
from discord.ext import commands
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from pygments import highlight, lexers, formatters
import ast
import sys
import json
import time
import readline
from builtins import input
import re
# on importe tout le nécessaire

intents = discord.Intents.default()
intents.members = True 
client_id=os.environ.get('client_UID')
client_secret=os.environ.get('SECRET')
DISCORD_TOKEN={os.environ.get('token')}
DISCORD_GUILD={os.environ.get('guild')}
Cooldown = 0


load_dotenv()
GUILD = os.getenv('DISCORD_GUILD')

discordclient = discord.Client(intents=intents)
liste = []

@discordclient.event
async def on_ready():
    for guild in discordclient.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{discordclient.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    channel = discord.utils.get(discordclient.get_all_channels(), guild__name='Le Bordel', name='chaine-de-mot') #on sélectionne le channel dans lequel on va prendre les messages, penser à pas modifier le salon (modo)
    async for texte in channel.history(limit=1000):
        if texte.author != discordclient.user:
            liste.append(texte.content) #on ajoute les messages à la liste
    print(liste[105))

 # on lance le bot
@discordclient.event
async def on_member_remove(member):
    print("left but dont care")
    channel = discordclient.get_channel(374612722849021962)
    await channel.send("https://tenor.com/view/oh-no-top-gear-jeremy-clarkson-no-one-cares-gif-18925814")

def school_API(message):
    ret = ""
    if "whereis" in message.content.lower():
        client = BackendApplicationClient(client_id=client_id)
        api = OAuth2Session(client=client)
        api_token = api.fetch_token(token_url='https://api.intra.42.fr/oauth/token', client_id=client_id, client_secret=client_secret)
        lien = message.content.lower()[8:]
        tmp = api.get('https://api.intra.42.fr/v2/users?filter[login]=' + lien)
        decode = json.loads(tmp.content.decode('utf-8'))
        if not decode:
            return (lien + " n'existe pas !")
        else:
            data = decode[0]
            if (data["location"] == None):
                return (lien + " n'est pas log !")
            else:
                return (lien + " est log en " + data["location"])
    elif "whoishere" in message.content.lower():
        client = BackendApplicationClient(client_id=client_id)
        api = OAuth2Session(client=client)
        api_token = api.fetch_token(token_url='https://api.intra.42.fr/oauth/token', client_id=client_id, client_secret=client_secret)
        tmp = api.get('https://api.intra.42.fr/v2/users?filter[login]=tnaton,bdetune,ghanquer,nflan,madelaha,nsartral')
        decode = json.loads(tmp.content.decode('utf-8'))
        i = 0;
        while (i < len(decode)):
            if (decode[i]["location"] != None):
               ret += (decode[i]["first_name"] + " est en " + decode[i]["location"] + '\n')
            i += 1
        if ret:
            return ret
        else:
            return "Il n'y a personne ! trop trop Sadge ! :sadge:"
        return ret

def Check_msg(message):
    ret = ""
    if ("SOCIETE" in message.content.upper() or "SOCIÉTÉ" in message.content.upper()):
        ret += "saussiéter\n"
    if "MILLION" in message.content.upper():
        print("MILLION")
        ret += "https://media1.tenor.com/images/e8fbc4408c8cbf27494788ee6ac08229/tenor.gif?itemid=24504749\n"
    if "D\'ACCORD" in message.content.upper():
        print("D\'ACCORD")
        ret += "https://tenor.com/view/asterix-vinalti-daccord-sure-ok-gif-15819283\n"
    if "DACCORD" in message.content.upper():
        print("DACCORD")
        ret += "https://tenor.com/view/asterix-vinalti-daccord-sure-ok-gif-15819283\n"
    if "QUOI" in message.content.upper():
        quoi=re.sub(r'[^a-zA-Z0-9]', '', message.content.upper())
        qlen = len(quoi)
        if (quoi[qlen-4] == "Q" and (quoi[qlen-3]) == "U" and (quoi[qlen-2]) == "O" and (quoi[qlen-1]) == "I"):
            print("feur")
            ret += "feur\n"
    if re.search('(^|([^0-9]+))42(([^0-9]+)|$)', message.content.upper()) != None:
        print(message.content.upper())
        wtf = ["42?", "Oh comme l'École", "Wtf tu connais l'École?!", "Oh 42 j'ai la ref", "42? 42? Comme l'École ?", "Oh 42 comme l'École mieux qu'Epitech ?"]
        ret += wtf[randint(0, len(wtf) - 1)] + '\n'
    if "BITE" in message.content.upper():
        print("BITE")
        bite = ["Bit", "Bite", "Shit", "Zizi", "Pipi", "Oui ?", "Chibre"] #Liste des réponses à bite
        ret += bite[randint(0, len(bite) - 1)] + '\n'
    if "ZIZI CACA" in message.content.upper(): #on vérifie que le bot à été ping
        print(len(liste))
        a = randint(0,len(liste)-1)
        print(a)
        response = liste[a] #on prend une réponse au hasard dans la liste
        print(response)
        ret += response + '\n' #on répond
    return ret

@discordclient.event
async def on_message(message): #quand un message est envoyé 
    if message.author != discordclient.user: #on vérifie que ce n'est pas un message du bot*
        if len(message.content) > 4 and message.content[1:4] == "an " and (message.content[0] == 'P' or message.content[0] == 'p'):
            for mention in message.mentions:
                if mention.id == 214463495415005184:
                    await message.channel.send("la balle a rebondit, effrayée par le charisme époustouflant de notre Suprême Leader, et s'est logée droit entre les deux yeux du traître qui l'a attaqué")
                    return
            print("PAN !")
            l = [", en plein dans le mille.", ", ça l'a touché.", ", headshot.", ", mais ça a raté.", ", mais il se tire dans le pied."] #Fin de phrase
            response = "<@" + str(message.author.id) + "> a tiré sur " + message.content[4:] + l[randint(0, len(l) - 1)]
            await message.channel.send(response)
        else:
            try:
                ret = school_API(message)
                if ret:
                    await message.channel.send(ret)
            except:
                await message.channel.send("Clef API morte !")
            ret = Check_msg(message)
            if ret:
                await message.channel.send(ret)
            if discordclient.user.mentioned_in(message) and message.mention_everyone is False:
                maybe=randint(0,1)
                if maybe==0:
                    print("non")
                    await message.channel.send("non")
                else:
                    print("oui")
                    await message.channel.send("oui")
discordclient.run(os.environ.get('token'))
