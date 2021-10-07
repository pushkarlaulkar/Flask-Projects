from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import json

app = Flask(__name__)
api = Api(app)

videos_put_args = reqparse.RequestParser()
videos_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
videos_put_args.add_argument("views", type=int, help="Views of the video", required=True)
videos_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

videos = [{"name":"tim", "views":"10", "likes":"10"}]

def abort_if_video_id_doesnt_exist(video_id):
	if(video_id not in videos):
		abort(404, message='Could not find Video...')

def abort_if_video_id_exist(video_id):
	if(video_id in videos):
		abort(409, message='Video already exists with that id...')

class Video(Resource):
	def get(self, video_id):
		#abort_if_video_id_doesnt_exist(video_id)
		return videos[video_id]
	
	def put(self, video_id):
		abort_if_video_id_exist(video_id)
		args = videos_put_args.parse_args()
		videos[video_id] = args
		return videos[video_id], 201
	
	def delete(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		del videos[video_id]
		return '', 204

api.add_resource(Video, "/videos/<int:video_id>")


if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True)