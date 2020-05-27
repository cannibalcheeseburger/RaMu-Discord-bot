import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='--')

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

@client.command(help="Returns Ping",description="Returns Ping")
async def ping(ctx):
    await ctx.send(f'Pencho! {round(client.latency *1000)} ms')

@client.command(aliases = ['8ball'],help="Return a response to the question",description="Return a response to the question")
async def _8ball(ctx, * ,question):
    responses = ["As I see it, yes.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don’t count on it.",
                "It is certain.",
                "It is decidedly so.",
                "Most likely.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Outlook good.",
                "Reply hazy, try again.",
                "Signs point to yes.",
                "Very doubtful.",
                "Without a doubt.",
                "Yes.",
                "Yes – definitely.",
                "You may rely on it.",
                "Tu PENCHOD HAI AUR KUCH NI"
                ]
    await ctx.send(f'Question: {question}\nAnswer:{random.choice(responses)}')

@client.command(help = "Returns maro mujhe maro x number of times",description="Returns maro mujhe maro x number of times")
async def oobhai(ctx,no):
    for i in range(int(no)):
        await ctx.send("Maro mujhe maro")
        if int(no) >10:
            break;

@client.command(help ="Clears x number of messages",description="Clears x number of messages")
async def clear(ctx,amount = 5):
    if amount<=5:
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send("Clear limit is 5")


client.run('NzE1MjA0NDU3NzU0Nzg3OTUy.Xs50Gg.z8fIxYd8ISJ3-PIkuChQV4pzUXw')

