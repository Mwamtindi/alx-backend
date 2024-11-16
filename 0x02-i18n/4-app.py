#!/usr/bin/env python3
"""
Flask application with Babel and forced locale parameter.
"""

from flask import Flask, render_template, request
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
    Select best match for supported lang's or use 'locale' parameter from URL.
    Returns:
        str: Best matching language code or forced language.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route for the index page.
    Returns:
        str: Rendered HTML content for index page.
    """
    return render_template('4-index.html', title=_("home_title"),
                           header=_("home_header"))


if __name__ == '__main__':
    app.run(debug=True)
