import requests



response= requests.get("https://docs.mathpix.com/",json={
    "src": "https://mathpix.com/examples/limit.jpg",
    "formats": ["text", "data", "html"],
    "data_options": {
        "include_asciimath": True,
        "include_latex": True}}
    , headers= {
    "content-type": "application/json",
    "app_id": "YOUR_APP_ID",
    "app_key": "YOUR_APP_KEY"})
