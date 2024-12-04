from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource): #created class with resource which will have a few different methods
    def get(self):
        return {"Hello World"} # newt step we register this as a resource:
    
api.add_resource(HelloWorld, "/helloworld") #added  name of the class

if __name__ == "__main__":
    app.run(debug=True) # in debug moods we see what is wrong
