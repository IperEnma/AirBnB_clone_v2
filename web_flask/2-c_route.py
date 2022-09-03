#!/usr/bin/python3
"""starts a Flask web app"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """send string to browser"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """send string to browser"""
    return 'HBNB'


@app.route('/c/<var>', strict_slashes=False)
def c(var):
    """capture variable"""
    var = var.replace("_", " ")
    return "C " + var


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
