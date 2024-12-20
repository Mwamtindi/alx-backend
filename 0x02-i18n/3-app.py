#!/usr/bin/env python3
"""
Flask application with Babel and translations
Module-sets up Flask app with Flask-Babel for internationalization
and implements translations using message IDs.
"""

from flask import Flask, render_template
from flask_babel import Babel, _


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
    return render_template('3-index.html', title=_("home_title"),
                           header=_("home_header"))


if __name__ == '__main__':
    app.run(debug=True)
