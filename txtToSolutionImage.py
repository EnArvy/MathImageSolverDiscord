import urllib.parse
import os
from dotenv import load_dotenv

#gets app id from .env
load_dotenv()
WOLFRAMID = os.getenv('WOLFAPPID')

baseurl = "http://api.wolframalpha.com/v1/simple"
urlappid = baseurl+"?appid="+WOLFRAMID

def getsolution(latex):
    finalurl = urlappid+"&input="+urllib.parse.quote(latex)
    return finalurl 
    