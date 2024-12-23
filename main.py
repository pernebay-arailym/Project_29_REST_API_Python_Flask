from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

#names = {"ary": {"age": 24, "gender": "female"},
         #"bill": {"age": 27, "gender": "male"}}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True) #mandatory arguments
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

videos = {}

def abort_if_video_id_doesnot_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video is is not valid...")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID...")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnot_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
       # print(request.form['likes'])
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self, video_id):
        abort_if_video_id_doesnot_exist(video_id)
        del videos[video_id]
        return '', 204

         

#class HelloWorld(Resource): #created class with resource which will have a few different methods
    #def get(self, name):
       # return names[name] # newt step we register this as a resource, JSON Format used, LOOK IF IT IS JSON SERIARISABLE 
    
    #def post(self):
        #print("POST request received!")  # Log the request
        #return {"data": "Posted"}
    
api.add_resource(Video, "/video/<int:video_id>") #added  name of the class

if __name__ == "__main__":
    app.run(debug=True) # in debug moods we see what is wrong
