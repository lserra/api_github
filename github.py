#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
# from tips.db import get_hashtags, get_tips
from bottle import (
    default_app, route, run, request, static_file, view, template
    )


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')


@route('/')
@route('/dashboard')
# @view('dashboard')
def dashboard():
    return template('dashboard')


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True, reloader=True)
