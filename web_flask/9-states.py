#!/usr/bin/python3
'''
    module to start a flask app
'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(error):
    '''
        tears down the session
    '''
    storage.close()


@app.route("/states", strict_slashes=False)
def states_list():
    '''returns a template of unordered lists of state
        objects
    '''
    return render_template("9-states.html", states=storage.all('State'))


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    states = storage.all('State')
    try:
        state_id = states[id]
        return render_template(
            '9-states.html',
            state_id=state_id,
            condition="state_id")
    except ValueError:
        return render_template('9-states.html', condition="not_found")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
