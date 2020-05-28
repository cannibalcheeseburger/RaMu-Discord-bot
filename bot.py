import discord
from discord.ext import commands
import random
import creds
from const import responses
import src


client = commands.Bot(command_prefix='--')

# EVENTS
@client.event
async def on_ready():
    await client.change_presence(status= discord.Status.online,activity=discord.Game('RaMu bhaiya Uth Gaye'))
    print('RaMu Bhaiya ki Jai.')

@client.event
async def on_member_join(member):
    print(f'Namaste {member} Bhaiya. Ajo Chai Peelo.')

@client.event
async def on_member_remove(member):
    print(f'{member} Bhaiya Chale gye. Paise kon de raha hai fir.')


# COMMANDS

## PING
@client.command(help="Returns Ping",description="Returns Ping")
async def ping(ctx):
    await ctx.send(f'Pencho! {round(client.latency *1000)} ms')

## 8 ball
@client.command(aliases = ['8ball'],help="Return a response to the question",description="Return a response to the question")
async def _8ball(ctx, * ,question):
    await ctx.send(f'Question: {question}\nAnswer:{random.choice(responses)}')

##OOBHAI
@client.command(help = "Returns maro mujhe maro x number of times",description="Returns maro mujhe maro x number of times")
async def oobhai(ctx,no:int):
    if no < 10:
        await ctx.send("Maro mujhe maro"*no)
    else:
        await ctx.send("Maro mujhe maro"*10)
    
## RECIPE
@client.command(help="Returns recipe of the day",description="Returns recipe of the day")
async def recipe(ctx):
    await ctx.send(src.recipe.recipeofday(creds.FOOD))


@client.command(help ="Clears x number of messages",description="Clears x number of messages")
async def clear(ctx,amount = 5):
    if amount<=5:
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send("Clear limit is 5")


client.run(creds.TOKEN)

