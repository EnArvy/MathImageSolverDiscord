# MathImageSolverDiscord

  Discord Bot to Get solution of math problems by uploading image in discord!
  
# Usage  
  
  After getting the bot on the server, use `)help` to access the help dialogue. 
  
  Use `)solve <imageurl>` to get solution of problem given via image at the given url.
  
  OR
  
  Use `)solve` and upload problem image in the same image.
  
# How It Works

 This bot is made in python.

 First, it gets the image url of the problem in input.
 
 Then it passes the url to mathpix api which is an ocr service and gets back the ocr results in the LaTeX format.
 
 Then it passes the result to wolfram simple api which solves the problem and returns the result(/s) as an image.
 
 The bot then sends this image to discord.

# Dependencies

  discord.py (use `pip install discord.py`)
  
  dotenv.py (use `pip install python-dotenv`)

  validators.py (use `pip install validators`)