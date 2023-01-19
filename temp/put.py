import requests

BASE = "http://127.0.0.1:5000/"

data = {"name": "VideoA", "views": 13, "likes": 123}

response = requests.put(f'{BASE}video/4', data)
print(response.json())