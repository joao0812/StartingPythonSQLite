import requests

BASE = "http://127.0.0.1:5000/"

data = {"name": "VideoA", "views": 13, "likes": 123}

response = requests.get(f'{BASE}video/1')
print(response.json())
input()
response = requests.put(f'{BASE}video/5', data)
print(response.json())