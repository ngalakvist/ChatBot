from chat import chat_bot
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
class ChatBot(Resource):
    def get(self,question):
        ans = chat_bot(question)
        return {"ans":ans}
        
api.add_resource(ChatBot, "/chatbot/<string:question>")

if __name__ == "__main__":

    app.run(debug=False)