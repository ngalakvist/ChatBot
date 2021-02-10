import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "chatbot/Jag har inte fått mitt användarID")
print(response.json())