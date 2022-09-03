#!/usr/bin/python3
"""starts a Flask web app"""


from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<var>')
def c(var):
    var = var.replace("_", " ")
    return var

app.run(host='0.0.0.0', port=5000)
