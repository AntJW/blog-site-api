from flask import jsonify, request
from werkzeug.security import check_password_hash
from utilities.token import generate_jwt

from app import app, conn


@app.route("/api/v1.0/auth/login", methods=["POST"])
def login():
    try:
        credentials = request.get_json()
        user = conn.connect("Users").find_one({"$or": [{"Email": credentials["Email"]},
                                                       {"Username": credentials["Email"]}]})

        if not user:
            return jsonify(error_message="Username or password is incorrect."), 401

        elif user:
            check_password = check_password_hash(user["Password"], credentials["Password"])
            if not check_password:
                return jsonify(error_message="Username or password is incorrect."), 401

            token = generate_jwt(user["_id"])
            return jsonify(success_message="Successful login!", token=token, acct=str(user["_id"])), 200
    except Exception:
        return jsonify(error_message="Sorry, error occurred. Please trying logging in again."), 500
