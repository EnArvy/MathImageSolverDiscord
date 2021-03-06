import os
from discord.ext import commands
import requests
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="'")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='mis',help='help dialogue')
async def getproblem(ctx,qimageurl=""):
    await ctx.send('hello')
    if qimageurl == "" and ctx.message.attachments:
        qimageurl = ctx.message.attachments[0].url
    await ctx.send(qimageurl)
    

          



bot.run(TOKEN)