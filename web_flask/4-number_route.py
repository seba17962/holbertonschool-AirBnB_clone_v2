#!/usr/bin/python3
"""
    task 2

    """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """_summary_
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """_summary_
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """_summary_
    """
    format_text = text.replace('_', ' ')
    return f'C {format_text}'


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is_cool'):
    """_summary_
    """
    format_python_text = text.replace('_', ' ')
    return f'Python {format_python_text}'


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """_summary_
    """
    try:
        n = int(n)
        return f"{n} is a number"
    except TypeError:
        return f"invalid literal for int() with base 10: {'n'}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
