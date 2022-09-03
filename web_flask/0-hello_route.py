#!/usr/bin/python3
"""module with hello world"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False



@app.route('/')
def index():
    return 'Hello HBNB!'

app.run(host='0.0.0.0', port=5000)
