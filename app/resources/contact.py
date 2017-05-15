from flask import request, jsonify
from utilities.email import send_email

from app import app


@app.route('/api/v1.0/message', methods=['POST'])
def contact_me():
    try:
        new_message = request.get_json()

        send_email(new_message["Name"], new_message["Email"], new_message["Phone"], new_message["Message"])
        return jsonify(success_message="Message Delivered."), 200
    except Exception:
        return jsonify(error_message="Sorry, error occurred. Please trying logging in again."), 500
