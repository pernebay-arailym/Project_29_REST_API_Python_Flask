from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#names = {"ary": {"age": 24, "gender": "female"},
         #"bill": {"age": 27, "gender": "male"}}

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    def put(self, video_id):
        print(request.form['likes'])
        return {}
         

#class HelloWorld(Resource): #created class with resource which will have a few different methods
    #def get(self, name):
       # return names[name] # newt step we register this as a resource, JSON Format used, LOOK IF IT IS JSON SERIARISABLE 
    
    #def post(self):
        #print("POST request received!")  # Log the request
        #return {"data": "Posted"}
    
api.add_resource(Video, "/video/<int:video_id>") #added  name of the class

if __name__ == "__main__":
    app.run(debug=True) # in debug moods we see what is wrong
