from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
#make a config -> where we save our database if in temp folder add ///tmp/:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse.db'
db = SQLAlchemy(app)

#create model to store videos:
class VideoModel(db.Model): #defining fields of the model
    id = db.Column(db.Integer, primary_key=True) #pr.key means this is a unique identify = id will be different for each video)
    name = db.Column(db.String(100), nullable = False) #nullable means without names, all should have signs
    views = db.Column(db.Integer, nullable= False)
    likes = db.Column(db.Integer, nullable= False)

    def __repr__(self):
        return "Video(name = {name}, views = {views}, likes = {likes})"
    
#with app.app_context():
#    db.create_all()
    
#names = {"ary": {"age": 24, "gender": "female"},
         #"bill": {"age": 27, "gender": "male"}}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True) #mandatory arguments
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required") #user send any of the arguments to update
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes of the video")


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,  #define what i want in this field
    'views': fields.Integer,
    'likes': fields.Integer
}
#videos = {}

#def abort_if_video_id_doesnot_exist(video_id):
#    if video_id not in videos:
#        abort(404, message="Video is is not valid...")
#
#def abort_if_video_exists(video_id):
#    if video_id in videos:
#        abort(409, message="Video already exists with that ID...")

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
       # print(request.form['likes'])
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video is taken...")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201


    def patch(self, video_id):
        args = video_put_args.parse_args()

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
