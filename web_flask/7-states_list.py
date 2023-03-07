#!/usr/bin/python3

from flask import Flask, render_template
import models
from models import storage
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    objs = models.storage.all(State)
    o_d = {o.id: o.name for k, o in objs.items()}
    return render_template('7-states_list.html', o_d=o_d)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
