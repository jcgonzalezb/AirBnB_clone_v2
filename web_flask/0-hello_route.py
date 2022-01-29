#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def hello():
    """Function that displays 'Hello HBNB!'"""
    return '"Hello HBNB!"'


if __name__ == "__main__":
    app.run(debug=True)
