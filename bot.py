import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is Ready.')

client.run('NzE1MjA0NDU3NzU0Nzg3OTUy.Xs50Gg.z8fIxYd8ISJ3-PIkuChQV4pzUXw')

