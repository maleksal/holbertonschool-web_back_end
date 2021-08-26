#!/usr/bin/env python3
"""route module"""

from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """match language function."""
    return request.accept_languages.best_match(app.config['en', 'fr'])


@app.route('/')
def index():
    """display html page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
