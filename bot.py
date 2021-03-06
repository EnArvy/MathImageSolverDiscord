import os
from discord.ext import commands
import requests
import json
from dotenv import load_dotenv
import imgToTxt
from imgToTxt import response


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  

bot = commands.Bot(command_prefix="'")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='mis',help='Send image file via url or upload via discord')
async def getproblem(ctx,qimageurl=""):
    await ctx.send('hello')
    if qimageurl == "" and ctx.message.attachments:
        qimageurl = ctx.message.attachments[0].url
    await ctx.send(qimageurl)
    query = '''{
    "src": qimageurl,
    "format": "data",
    "data_options":{
        "include_latex": true
    }'''
    print(response)
    latex = json.dumps(json.loads(response.data))   
    print(latex)


bot.run(TOKEN)