#!/usr/bin/python3

from flask import Flask, render_template
import models
from models.city import City
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    models.storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    s = [o for o in models.storage.all(State).values()]
    a = [o for o in models.storage.all(Amenity).values()]
    return render_template('10-hbnb_filters.html', s=s, a=a)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
