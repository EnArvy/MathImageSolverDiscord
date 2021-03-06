import os
from discord.ext import commands
import requests
import json
from dotenv import load_dotenv
from imgToTxt import getlatex
from txtToSolutionImage import getsolution



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  

bot = commands.Bot(command_prefix="'")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='mis',help='Send image file via url or upload via discord')
async def getproblem(ctx,qimageurl=""):
    
    if qimageurl == "" and ctx.message.attachments:
        qimageurl = ctx.message.attachments[0].url
    

    response = getlatex(qimageurl).json()
    latex = response['latex']
    answer = getsolution(latex)
    await ctx.send(answer)


bot.run(TOKEN)
