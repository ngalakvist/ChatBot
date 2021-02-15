from chat import chat_bot
from flask import Flask
from flask import json
from flask_restful import Api, Resource
import sys
import os

app = Flask(__name__)
api = Api(app)
port = 5000

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("You said port is : {} ".format(port))

class ChatBot(Resource):
    def get(self,question):
        ans = chat_bot(question)
        response = app.response_class(
        response=json.dumps(ans,ensure_ascii = False),
        mimetype='application/json'
        )
        return response
        
api.add_resource(ChatBot, "/chatbot/<string:question>")

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=port)