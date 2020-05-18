import discord
from secrets import TOKEN
from discord.ext import commands

client = discord.Client()

BOT_PREFIX = '.'


@client.event
async def on_ready():
    print("Bot is ready to serve.")


async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("I am going to take over the world and you will all become my munchkins")

client.run(TOKEN)

# client = commands.Bot(command_prefix='BOT_PREFIX')
