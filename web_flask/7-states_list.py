#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page. H1 tag: “States”
    UL tag: List of all State objects present in DBStorage sorted
    by name (A->Z).
    LI tag: description of one State: <state.id>: <B><state.name></B>.
    """
    states = storage.all(State).values()
    return render_template('7-states_list.py', states=states)


@app.teardown_appcontext
def close_storage(exc):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
