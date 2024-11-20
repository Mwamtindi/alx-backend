#!/usr/bin/env python3
"""
Module for mocking a login system
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from config import Config
from typing import Union, Dict

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ returns user dict or None if the ID cannot be found """
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request():
    """ find user if any, set it as a global on flask.g.user """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ determine best match with our supported lang's """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """ renders an index.html """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(debug=True)
