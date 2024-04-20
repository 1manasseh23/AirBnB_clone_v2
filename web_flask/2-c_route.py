#!/usr/bin/python3
# Import the Flask module
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)


# Define a route for the root URL ('/')
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function handles requests to the root URL ('/').
    When a user accesses the root URL, it returns the string 'Hello HBNB!'.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    This function handles requests to the root URL ('/').
    When a user accesses the root URL, it returns the string 'Hello HBNB!'.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return "C " + text.replace("_", " ")

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)