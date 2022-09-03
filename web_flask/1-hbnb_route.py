#!/usr/bin/python3
"""starts a flask web app"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """send string to browser"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """send string to browser"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
