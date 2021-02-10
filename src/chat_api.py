from flask import Flask
from flask_restful import Api, Resource,request
app = Flask( __name__)
api = Api(app)
class ChatBot(Resource):
    def get(self,question):
        return {"data":question}
        
api.add_resource(ChatBot, "/question/<string:question>")

if __name__== " __chat_api__":
    app.run(debug=True)