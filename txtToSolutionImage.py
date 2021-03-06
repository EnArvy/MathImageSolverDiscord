import wolframalpha
import os
from dotenv import load_dotenv

load_dotenv()
WOLFRAMID = os.getenv('WOLFAPPID')
client = wolframalpha.Client(WOLFRAMID)

def getsolution(latex):
    res = client.query(latex)
    answer = next(res.results).text 
    return(answer)