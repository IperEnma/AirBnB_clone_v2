#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(exception):
    """close session current"""
    storage.close()


@app.route('/states_list')
def states_list():
    """send object state to template"""
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        states = storage.all(State)
        states_list = []
        for key, state in states.items():
            states_list.append(state)
        states_list.sort(key=lambda x: x.name)
        return render_template("7-states_list.html", states=states_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
