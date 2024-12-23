from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

#names = {"ary": {"age": 24, "gender": "female"},
         #"bill": {"age": 27, "gender": "male"}}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video") #mandatory arguments
video_put_args.add_argument("views", type=int, help="Views of the video")
video_put_args.add_argument("likes", type=int, help="Likes of the video")

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    def put(self, video_id):
       # print(request.form['likes'])
        args = video_put_args.parse_args()
        return {video_id: args}
         

#class HelloWorld(Resource): #created class with resource which will have a few different methods
    #def get(self, name):
       # return names[name] # newt step we register this as a resource, JSON Format used, LOOK IF IT IS JSON SERIARISABLE 
    
    #def post(self):
        #print("POST request received!")  # Log the request
        #return {"data": "Posted"}
    
api.add_resource(Video, "/video/<int:video_id>") #added  name of the class

if __name__ == "__main__":
    app.run(debug=True) # in debug moods we see what is wrong
