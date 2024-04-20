#!/bin/python3

from flask import Flask

server = Flask(__name__)

@server.route("/hello")
def test():
    """
    Showcase a simple `hello world` program to prove we can
    run webpages from android.
    """
    return "Hello World."
