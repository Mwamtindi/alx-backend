#!/usr/bin/env python3
"""
Flask application module
This module sets up a basic Flask application with a single route.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Route for the index page.
    Returns:
        str: Rendered HTML content for index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
