import requests
import urllib.parse
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
baseurl = "http://api.wolframalpha.com/v1/simple"
WOLFRAMID = os.getenv('WOLFAPPID')
urlappid = baseurl+"?appid="+WOLFRAMID


def getsolution(latex):
    finalurl = urlappid+"&input="+urllib.parse.quote(latex)

    return finalurl 
    