#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)

"""Defines the route"""


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Returns C followed by by the value of the text"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    """Starts the flask development server"""
    app.run(host='0.0.0.0', port=5000)
