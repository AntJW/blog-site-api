from flask import Response, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
from pymongo import DESCENDING
from utilities.helpers import get_authorized_headers
from app import app, conn


@app.route('/api/v1.0/posts', methods=['GET'])
def get_posts():
    queried_results = dumps(conn.connect('Posts').find().sort("CreatedOn.DatetimeUTC", DESCENDING))
    return Response(queried_results, content_type="application/json")


@app.route('/api/v1.0/posts/<string:post_id>', methods=['GET'])
def get_single_post(post_id):
    queried_results = dumps(conn.connect('Posts').find({"_id": ObjectId(str(post_id))}))
    return Response(queried_results, content_type="application/json", status=200)


@app.route('/api/v1.0/posts/new', methods=['POST'])
def create_new_post():
    try:
        acct_id, client_utc, client_utc_offset = get_authorized_headers()
    except Exception:
        return jsonify(error_message="Unauthorized request. Please ensure you are logged in."), 401

    try:
        new_post = request.get_json()
        author_first_name = "Anthony"
        author_last_name = "White"
        date_time_utc = new_post["CreatedOn"]["DatetimeUTC"]
        offset = new_post["CreatedOn"]["TimeOffset"]

        post_id = conn.connect('Posts').insert({"Title": new_post["Title"], "Body": new_post["Body"], "Author":
            {"FirstName": author_first_name, "LastName": author_last_name}, "CreatedOn":
            {"DatetimeUTC": datetime.strptime(date_time_utc, '%Y-%m-%dT%H:%M:%S.%fZ'), "TimeOffset": offset},
                                                "Tags": new_post["Tags"]})
        return jsonify(post_id=str(post_id)), 200
    except Exception:
        return jsonify(error_message="Sorry, error occurred. Please trying logging in again."), 500
