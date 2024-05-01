# This example requires the 'message_content' intent.

import discord #Duh, Obviously
import json #helps in working with json files
import requests #Does request to API and stuff
import random #nothing is better than randomness after all. Entropy is the law of universe.

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#List of Sad words to automatically respond to
sad_words=["feel sad","am depressed","feel sick","urgh"]
#Phrases it can respond with
starter_encouragements = [
  "Cheer up! You can get through this my guy.",
  "Hang in there. After all, Duty ends only in death.",
  "You are a great fella!",
  "Look around you. Life is bad only if you let it. Let go, take a breathe, AND LETS FUCKING GOOO"
]


#This function requests from the given rl and stores it in the Json file. This it extracts it from the JSon file in a specefic format, isuppose?
def get_quote():
    response= requests.get("https://zenquotes.io/api/random")
    json_data=json.loads(response.text)
    quote=json_data[0]['q']+"-"+json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg=str.lower(message.content)

    if msg.startswith('$inspire'):
        quote=get_quote()
        await message.channel.send(quote)

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if msg.__len__()>200:
        await message.channel.send('🤓')

with open('token.txt','r') as file:
    token=file.read()
client.run(token)