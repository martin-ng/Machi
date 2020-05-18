import discord
import random
from secrets import TOKEN
from discord.ext import commands

# client = discord.Client()
# BOT_PREFIX = '.'
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("Bot is ready to serve.")


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')
    print(f'こんにちは, {member}')


# @client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
    print(f'じゃあまたね, {member}')


# @client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("what"):
        pass


@client.command()
async def ping(ctx):
    await ctx.send('Pong')


@client.command(aliases=['machi'])
async def questions(ctx, *, question):
    responses = ['I dunno, will you?', 'heh', 'likely!', 'no.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


client.run(TOKEN)
