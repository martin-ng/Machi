import discord
import random
from secrets import TOKEN
from discord.ext import commands

description = "An example bot"

bot = commands.Bot(command_prefix='.', description=description)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print('-------')
    print("Bot is ready to serve.")


# @client.event
# async def on_message(message):
#     sharone_responses = [
#         'Hi', 'Hello', 'im not a robot i swear!', 'Good day to you']

#     if str(message.author) == 'sharone#7062':
#         await message.channel.send(random.choice(sharone_responses))


# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined a server.')
#     print(f'こんにちは, {member}')


# @client.event
# async def on_member_remove(member):
#     print(f'{member} has left the server.')
#     print(f'じゃあまたね, {member}')


# @client.event
# async def on_message(message):
#     message.content.lower()
#     if message.author == client.user:
#         return
#     if message.content.startswith("what"):
#         pass

@bot.command()
async def add(ctx, *args):
    # bot command that adds two numbers
    argLength = len(args)
    if argLength < 1:
        return 0
    sumOfArgs = 0
    for num in args:
        sumOfArgs += num
    await ctx.send(f'The sum is {sumOfArgs}')


@bot.command()
async def average(ctx, *args):
    return sum(args)/len(args)


@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@bot.command(aliases=['machi'])
async def questions(ctx, *, question):
    responses = ['I dunno, will you?', 'heh', 'likely!', 'no.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

bot.run(TOKEN)
