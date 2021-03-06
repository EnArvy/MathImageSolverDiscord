import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()


true = "true"

APPID = os.getenv('APP_ID')
APPKEY = os.getenv('APP_KEY')
mathpixurl = 'https://api.mathpix.com/v3/text'  
def getlatex(qimageurl) :
 
    response = requests.post(mathpixurl,
               data=json.dumps({"src": qimageurl}),
               headers={"app_id":APPID,"app_key":APPKEY,"Content-Type": "application/json"})
             
    return response    
