import os
import io
import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv
from imgToTxt import getlatex
from txtToSolutionImage import getsolution
import validators

#Gets token from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  

bot = commands.Bot(command_prefix="Go ",help_command=None)

#better help
@bot.command(name='help')
async def help(ctx):
    await ctx.send("""  Welcome to the MathImageSolver Bot!
    
    Use this bot to get solution of math problems via image!
      
    Use )help to show this help dislogue
    Use )mis <imageurl> OR 'mis with image file attached to get solution as an image!"""  )

#Marks succesful connection
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name='Go help'))

#command to get solution upon input of picture/url with math problem
@bot.command(name='solve')
async def getproblem(ctx,qimageurl=""):
    
    #checks if url sent otherwise gets attachment image url
    if qimageurl == "" and ctx.message.attachments:
        qimageurl = ctx.message.attachments[0].url
    #cheks if url is valid
    valid=validators.url(qimageurl)
    if valid != True:
        await ctx.send("Enter Valid URL")
    else:
        latex = getlatex(qimageurl)  #calling ocr api and getting result in latex format
        solution = getsolution(latex) #get the url of api result
        #get image from url and send to discord
        async with aiohttp.ClientSession() as session:
            async with session.get(solution) as resp:
                data = io.BytesIO(await resp.read())
        await ctx.send(file=discord.File(data, 'Solution.png'))

bot.run(TOKEN)
