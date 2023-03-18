import discord
from discord import app_commands
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
import json
from typing import List
import asyncio

import requests

load_dotenv()

# TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is Up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def testinput(ctx):
    embeds = [
        Embed(title="test page 1", description="This is just some test content!", color=0x115599),
        Embed(title="test page 2", description="Nothing interesting here.", color=0x5599ff),
        Embed(title="test page 3", description="Why are you still here?", color=0x191638)
    ]

async def main():
    await load()
    await bot.start(os.getenv('DISCORD_TOKEN'))

asyncio.run(main())









# @bot.tree.command(name="findepisode")
# @app_commands.describe(person = "Who do you want to learn about?")
# async def say(interaction: discord.Interaction, person: str):
#     jsontosend = {
#     "fields": ["people_tostring"],
#     "queries": [person]
#     }
#     personsearch = requests.post("https://62fm88kr45.execute-api.us-east-1.amazonaws.com/prod/standardquery", data = json.dumps(jsontosend))
#     formatresp = json.loads(personsearch.text)
#     formatbody = json.loads(formatresp['body'])
#     episode_array = []
#     for i in formatbody:
#         episode_array.append(i)
#     if len(episode_array) > 0:
#         messagestring = "\n * ".join(episode_array)
#         message = f"`{person}` is in episodes: \n* {messagestring}"
#     else:
#         message = "Nothing found!"
#     await interaction.response.send_message(message)


# @app_commands.describe(topic = "What topic are you interested in?")
# async def say(interaction: discord.Interaction, topic: str):
#     jsontosend = {
#     "fields": ["topics_tostring"],
#     "queries": [topic]
#     }
#     personsearch = requests.post("https://62fm88kr45.execute-api.us-east-1.amazonaws.com/prod/standardquery", data = json.dumps(jsontosend))
#     formatresp = json.loads(personsearch.text)
#     formatbody = json.loads(formatresp['body'])
#     episode_array = []
#     for i in formatbody:
#         episode_array.append(i)
#     if len(episode_array) > 0:
#         messagestring = "\n * ".join(episode_array)
#         message = f"`{topic}` is discussed in episodes: \n* {messagestring}"
#     else:
#         message = "Nothing found!"
#     await interaction.response.send_message(message)

# @app_commands.describe(alexsays = "Alex says...?")
# async def say(interaction: discord.Interaction, alexsays: str):
#     jsontosend = {
#     "fields": ["alex_says_tostring"],
#     "queries": [alexsays]
#     }
#     personsearch = requests.post("https://62fm88kr45.execute-api.us-east-1.amazonaws.com/prod/standardquery", data = json.dumps(jsontosend))
#     formatresp = json.loads(personsearch.text)
#     formatbody = json.loads(formatresp['body'])
#     episode_array = []
#     for i in formatbody:
#         episode_array.append(i)
#     if len(episode_array) > 0:
#         messagestring = "\n * ".join(episode_array)
#         message = f"Alex says `{alexsays}` in these episodes: \n* {messagestring}"
#     else:
#         message = "Nothing found!"
#     await interaction.response.send_message(message)




# bot.run(os.getenv('DISCORD_TOKEN'))