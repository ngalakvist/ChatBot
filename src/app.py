from chat import chat_bot
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
 
@app.route("/")
def chat():
    return {"Hello Chat bot"}

