from flask import jsonify, request
from app import app, conn
from datetime import datetime


@app.route('/api/v1.0/log', methods=['POST'])
def log_ui_event():
    # Levels: error, warning, info
    # Message: user created log message
    # Event: system generated log
    # Origin: web, mobile
    event = request.get_json()
    conn.connect('Logs').insert({"CreatedOn": datetime.utcnow(), "Level": event['level'],
                                 "Message": event['message'], "Event": event['event'], "Origin": event['origin']})
    return jsonify(code=200)


def log_event(message, event, level):
    # Levels: error, warning, info
    # Message: user created log message
    # Event: system generated log
    # Origin: api
    conn.connect('Logs').insert({"CreatedOn": datetime.utcnow(), "Level": level,
                                 "Message": message, "Event": event, "Origin": "api"})
