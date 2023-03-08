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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    objs = models.storage.all(State)
    if id:
        o_d = [o for o in objs.values() if id == o.id]
    else:
        o_d = [o for o in objs.values()]
    return render_template('9-states.html', o_d=o_d, n=len(o_d))

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
