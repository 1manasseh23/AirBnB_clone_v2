#!/usr/bin/python3
"""Import the Flask module"""
from flask import Flask

app = Flask(__name__)


"""Define a route for the root URL ('/')"""
@app.route('/', strict_slashes=False)
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb()
    return 'HBNB'
	

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

