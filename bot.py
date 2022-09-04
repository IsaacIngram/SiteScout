import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv('secrets.env')
TOKEN = os.getenv('DISCORD_TOKEN')

# Choose bot intents
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("Logged in!")
