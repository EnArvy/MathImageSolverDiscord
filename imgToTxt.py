

mathpixurl = 'https://api.mathpix.com/v3/latex' 

query = '''{
    "src": qimageurl,
    "format": "data",
    "data_options":{
        "include_latex": true
    }'''
response = requests.post(
            mathpixurl,
            data=json.dumps(query),
            headers={
                "app_id": os.getenv('APP_ID'),
                "app_key": os.getenv('APP_KEY'),
                "Content-Type": "application/json"
            }
        )
