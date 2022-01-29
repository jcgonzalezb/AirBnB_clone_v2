#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index():
    """Function that displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', methods=("GET", "POST"), strict_slashes=False)
def hbnb():
    """Function that displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', methods=("GET", "POST"), strict_slashes=False)
def text(text):
    """Display “C” followed by the value of the text variable"""
    return "C {}".format(escape(text.replace("_", " ")))


@app.route('/python/<text>', methods=("GET", "POST"), strict_slashes=False)
def python_text(text='is cool'):
    """Display “Python” followed by the value of the text variable"""
    return "Python {}".format(escape(text.replace("_", " ")))


@app.errorhandler(404)
def page_not_found(e):
    return "Python is cool"


if __name__ == "__main__":
    app.run(debug=True)
