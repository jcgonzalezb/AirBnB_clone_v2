#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template


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
    """Display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_if_int(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """Display a HTML page only if n is an integer.
    Display if the number is odd or even"""
    if isinstance(n, int):
        if (n % 2) == 0:
            context = {
                'n': n,
                'm': "even"
            }
        else:
            context = {
                'n': n,
                'm': "odd"
            }
        return render_template('6-number_odd_or_even.html', **context)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
