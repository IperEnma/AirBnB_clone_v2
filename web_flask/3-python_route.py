#!/usr/bin/python3
"""starts a Flask web app"""


from flask import Flask, request


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c(var):
    text = text.replace("_", " ")
    return var

@app.route('/python', defaults={'text': "is_cool"})
@app.route('/python/<text>')
def python(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)

app.run(host='0.0.0.0', port=5000)
