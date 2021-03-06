import requests
import os
import json
from dotenv import load_dotenv



load_dotenv()
mathpixurl = 'https://api.mathpix.com/v3/latex' 



APPID = os.getenv('APP_ID')
APPKEY = os.getenv('APP_KEY') 
def getlatex(qimageurl) :

    response = requests.post(
            mathpixurl,
            data=json.dumps({
                                "src": qimageurl,
                                "format": "data",
                                "data_options":{
                                    "include_latex": true
                            }}
                        ),
            headers={
                "app_id":APPID,
                "app_key":APPKEY,
                "Content-Type": "application/json"
            }
        )
    return response    
