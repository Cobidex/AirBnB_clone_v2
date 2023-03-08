#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def Hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C {}'. format(text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='cool'):
    return 'Python {}'. format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def n_var(n):
    return '{} is a number'. format(n)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
