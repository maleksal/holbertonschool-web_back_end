#!/usr/bin/env python3
"""myroute module"""

from flask import Flask, render_template, request
from flask_babel import Babel
from flask import g

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Configurations for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def hello():
    """render html file"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """determine language."""
    locale = request.args.get("locale")
    log_as = request.args.get('login_as')
    _locale = request.headers.get('locale')

    if locale:
        return locale

    if log_as:
        locale = users[int(log_as)]['locale']
        if locale:
            return locale

    if _locale:
        return _locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    '''Returns user from'''
    try:
        return users[int(request.args.get('login_as'))]
    except Exception:
        return None


@app.before_request
def before_request():
    '''set a user.'''
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    ''' timezone '''
    time = request.args.get('timezone')
    if time in pytz.all_timezones:
        return time
    else:
        user_id = request.args.get('login_as')
        time = users[int(user_id)]['timezone']
        if time in pytz.all_timezones:
            return time
        raise pytz.exceptions.UnknownTimeZoneError
    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
