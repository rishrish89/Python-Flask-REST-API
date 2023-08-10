from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    likes = db.Column(db.Integer, nullable = False)
    views = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"


#db.create_all() (run it only once)




video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name',type=str,required=True,help="Name of the video is required")
video_put_args.add_argument('views',type=int,required=True,help="views of the video is required")
video_put_args.add_argument('likes',type=int,required=True,help="likes of the video is required")


video_update_args = reqparse.RequestParser()
video_update_args.add_argument('name',type=str,help="Name of the video is required")
video_update_args.add_argument('views',type=int,help="views of the video is required")
video_update_args.add_argument('likes',type=int,help="likes of the video is required")





resource_field = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class Video(Resource):

    @marshal_with(resource_field)
    def get(self,video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message = "Could not find video with that id")
        return result

    @marshal_with(resource_field)
    def put(self,video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if result:
            abort(409, message = "Video id is taken")

        video = VideoModel(id = video_id, name = args['name'], likes = args['likes'], views = args['views'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_field)
    def patch(self,video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message = "Video doesnt exist ,cannot update")


        if "name" in args and args['name'] != None: 
            result.name = args['name']
        if 'likes' in args and args['likes'] !=  None:
            result.likes = args['likes']
        if 'views' in args and args['views'] != None:
            result.views = args['views']

        db.session.commit()
        return result




#didnt delete command left to work on for data base 
    def delete(video_id):
        abort_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return "", 204







api.add_resource(Video,"/video/<int:video_id>")


if __name__=='__main__':
    app.run(debug=True)

