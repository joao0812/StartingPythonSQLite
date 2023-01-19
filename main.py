from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort
import sqlite3
import json

import uuid

banco = sqlite3.connect('videos.db')
cursor = banco.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS videos (id INTEGER, name TEXT, views INTEGER, likes INTEGER)")
# cursor.execute("INSERT INTO videos VALUES(3, 'videoF', 200, 2)")
# banco.commit()


def get_columns():
    c = sqlite3.connect('videos.db').cursor()
    all_id = c.execute("SELECT id FROM videos").fetchall()
    ids = [data[0] for data in all_id]
    print(ids)
    return ids

# desc = [description[0] for description in cursor.description]
# print(desc)


video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "name", type=str, help="Name of the Video is required", required=True)
video_put_args.add_argument(
    "likes", type=int, help="Like on the Video is required", required=True)
video_put_args.add_argument(
    "views", type=int, help="Views of the Video is required", required=True)


def verify_id_doesnt_exist(video_id):
    ids = get_columns()
    if video_id not in ids:
        abort(404, message="Video ID is not exist...")


def verify_id_exist(video_id):
    ids = get_columns()
    if video_id in ids:
        abort(409, message="Video ID already exist...")


app = Flask(__name__)
api = Api(app)


class Video(Resource):
    def get(self, video_id):
        print(video_id)
        verify_id_doesnt_exist(video_id)
        c = sqlite3.connect('videos.db').cursor()
        c.execute(f"SELECT * FROM videos WHERE id = {video_id}")
        data = c.fetchall()
        return jsonify(data)

    def put(self, video_id):
        verify_id_exist(video_id)
        args = video_put_args.parse_args()
        banco = sqlite3.connect('videos.db')
        c = banco.cursor()
        c.execute(f"INSERT INTO videos(id, name, views, likes) VALUES(?, ?, ?, ?)", (video_id, args['name'], args['views'], args['likes']))
        banco.commit()
        return args


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
