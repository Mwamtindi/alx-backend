#!/usr/bin/env python3
"""
Flask application with Babel and locale selection.
Module-sets up Flask app with Flask-Babel for internationalization
and implements locale selection based on client request headers.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask app and Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Selects best match for supported lang's based on req headers.
    Returns:
        str: Best matching language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route for the index page.
    Returns:
        str: Rendered HTML content for index page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
