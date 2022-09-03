#!/usr/bin/python3
"""starts a Flask web app"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """set string to browser"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """set string to browser"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(var):
    """capture variable"""
    text = text.replace("_", " ")
    return var


@app.route('/python', defaults={'text': "is_cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """capture variable and set value"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """is number or not"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """is number or not template"""
    number = "Number: {}".format(n)
    return render_template('5-number.html', number=number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
