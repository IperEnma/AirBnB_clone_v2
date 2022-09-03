#!/usr/bin/python3
"""starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.city import City
from models.state import State
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(exception):
    """close current session"""
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """return cities by states"""
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        states = storage.all(State)
        states_list = []
        for key, state in states.items():
            states_list.append(state)
        states_list.sort(key=lambda x: x.name)
        return render_template("8-cities_by_states.html", states=states_list)
    else:
        cities = storage.all(City)
        states = storage.all(State)
    return render_template(
            "8-cities_by_states.html",
            states=states,
            cities=cities)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
