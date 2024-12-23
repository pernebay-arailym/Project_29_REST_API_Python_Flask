from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"ary": {"age": 24, "gender": "female"},
         "bill": {"age": 27, "gender": "male"}}

class HelloWorld(Resource): #created class with resource which will have a few different methods
    def get(self, name):
        return names[name] # newt step we register this as a resource, JSON Format used, LOOK IF IT IS JSON SERIARISABLE 
    
    #def post(self):
        #print("POST request received!")  # Log the request
        #return {"data": "Posted"}
    
api.add_resource(HelloWorld, "/helloworld/<string:name>") #added  name of the class

if __name__ == "__main__":
    app.run(debug=True) # in debug moods we see what is wrong
