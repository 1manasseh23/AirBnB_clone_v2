#!/usr/bin/python3
""" This module conatins a simple Flask App """
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return f'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    if '_' in text:
        text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text='is cool'):
    if '_' in text:
        text = text.replace('_', ' ')
    return f'Python {escape(text)}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{escape(n)} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
