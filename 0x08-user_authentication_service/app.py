#!/usr/bin/env python3
"""route module for API"""

from auth import Auth
from flask import Flask, jsonify, request


app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'])
def hi():
    """root route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """implements POST /users route."""
    email, password = (
        request.form.get('email'),
        request.form.get('password')
    )

    try:
        check_user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})\
            if check_user else None

    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
