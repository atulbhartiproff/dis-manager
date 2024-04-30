# This example requires the 'message_content' intent.

import discord
import sys #This is to import token file

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

sys.path.append('C:\Users\harsh\OneDrive\Documents\College Stuff')
with open('Token for discord bot.txt','r') as file:
    token=file.read()
client.run(token)
