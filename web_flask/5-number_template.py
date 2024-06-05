#!/usr/bin/python3
"""
Starts Flask web app.

Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
    /python/<text> - display "Python <text>"
    /number_template/<n> - display an HTML page if n is an integer.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnbb_home():
    """Displays 'Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Display 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C ' followed by text content,
    Replaces underscore in the text with spaces.

    Args:
        text (str): The text to display.

    Returns:
        str: The formatted string with underscore replaced by spacaes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays 'Python ' followed by the content of the text.

    Replaces underscores in the text with spaces.
    Default text is 'is cool'.

    Args:
        text (str): The text to display, 'is cool' by default.

    Returns:
        str: The formatted string with underscores replacred by spaces.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    Displays an HTML page  only if n is an integer.

    Args:
        n (int): The number to display.

    Returns:
        str: The formatted string confirming  n is a number.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
