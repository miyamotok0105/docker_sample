#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify

app = Blueprint(
    'hoge',
    __name__,
    url_prefix='/hoge'
)

@app.route('/test')
def hoge():
    return "\nhogehoge"
