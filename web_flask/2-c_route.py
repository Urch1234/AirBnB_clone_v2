#!/usr/bin/python3
"""
Starts a Flask web applicaion.

The application listens on 0.0.0.0:5000
Routes:
    /: displays "Hello HBNB!"
    /hbnb: displays "HBNB"
    /c/<text>: display "C " followed by the value of the text
    Variable (replace underscore _ symbol with space).
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_home():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Displays HBNB"""
    return "HBNB"


@app.route('/hbnb/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays 'C ' followed by the value of the text variable
    """
    text = text.replace('_', ' ')
    return "C %s" % text


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
