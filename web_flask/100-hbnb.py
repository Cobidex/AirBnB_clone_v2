#!/usr/bin/python3

from flask import Flask, render_template
import models
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    models.storage.close()

@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    s = [o for o in models.storage.all(State).values()]
    a = [o for o in models.storage.all(Amenity).values()]
    p = [o for o in models.storage.all(Place).values()]
    u = [o for o in models.storage.all(User).values()]
    return render_template('100-hbnb.html', s=s, a=a, p=p, u=u)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
