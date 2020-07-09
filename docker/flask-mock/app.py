import json
from typing import Any, Dict

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

basic_auth_users = {"mock_user": "mock_pass"}


@auth.get_password
def get_pw(username: str) -> Any:
    if username in basic_auth_users:
        return basic_auth_users.get(username)
    return None


@app.route("/material", methods=["GET"])
@auth.login_required
def material() -> Any:
    return jsonify({"body": "OK"})


@app.route("/echo", methods=["POST"])
@auth.login_required
def echo() -> Any:
    message: Dict[str, Any] = json.loads(request.data)
    return jsonify({"body": json.dumps(message)})


app.run()
