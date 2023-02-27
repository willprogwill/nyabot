import discord
from discord.ext import commands

TOKEN = 'MTA3OTgxNzY2MjgwMjE4MjI4NA.G1xnEJ.Ag5TrgjbWuTUgJ8hcU6NuRr8OAexhtSg_a_i8I' # TOKENを貼り付け

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

@client.command()
async def nya(ctx):
    await ctx.send('にゃん')

client.run(TOKEN)
