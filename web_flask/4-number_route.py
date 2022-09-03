#!/usr/bin/python3
"""starts a Flask web app"""
from flask import Flask, request


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """send string to browser"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """send string to browser"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(var):
    """capture variable"""
    text = text.replace("_", " ")
    return var


@app.route('/python', defaults={'text': "is_cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """capture variable a set default"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """is number or not"""
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
