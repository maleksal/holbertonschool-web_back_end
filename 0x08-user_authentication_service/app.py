#!/usr/bin/env python3
"""route module for API"""

from auth import Auth
from flask import Flask, jsonify


app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'])
def hi():
    """root route"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
