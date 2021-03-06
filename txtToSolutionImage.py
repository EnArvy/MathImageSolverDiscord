import requests
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()
baseurl = "http://api.wolframalpha.com/v1/simple"
WOLFRAMID = os.getenv('WOLFAPPID')
urlappid = baseurl+"?appid="+WOLFRAMID


def getsolution(latex):
    finalurl = urlappid+"&input="+'"'+latex+'"'


    return finalurl 
    