import os
import io
import aiohttp
import discord
from discord.ext import commands
import requests
import json
from dotenv import load_dotenv
from imgToTxt import getlatex
from txtToSolutionImage import getsolution
import validators


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
    
    valid=validators.url(qimageurl)
    if valid == False:
        print("Enter Valid URL")
        return None

    response = getlatex(qimageurl).json()
    latex = response['latex']
    solution = getsolution(latex)
    async with aiohttp.ClientSession() as session:
        async with session.get(solution) as resp:
            data = io.BytesIO(await resp.read())
            await ctx.send(file=discord.File(data, 'Solution.png'))


bot.run(TOKEN)
