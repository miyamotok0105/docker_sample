#!/usr/bin/python
# -*- coding: utf-8 -*-
from server import app

@app.route('/')
def hello():
    return "Hello"

if __name__ == '__main__':
    app.run()

