#!/usr/bin/python3
"""show 6-index.html"""
from flask import Flask, render_template
from os import getenv
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(exception):
    """close current session"""
    storage.close()


@app.route('/hbnb_filters')
def states():
    """return airbnb template"""
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        states = storage.all(State)
        states_list = []
        for key, state in states.items():
            states_list.append(state)
        states_list.sort(key=lambda x: x.name)
        return render_template("10-hbnb_filters.html", states=states_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
