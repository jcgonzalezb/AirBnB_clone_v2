#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask

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
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python')
@app.route('/python/<text>', methods=("GET", "POST"), strict_slashes=False)
def python_text(text='is cool'):
    """Display “Python” followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', methods=("GET", "POST"), strict_slashes=False)
def number(n):
    """Display display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
