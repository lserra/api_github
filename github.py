#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
# from tips.db import get_hashtags, get_tips
from bottle import (
    default_app, route, run, request, static_file, view, template, error
    )
from repos.db import get_rows_count


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')


@route('/')
@route('/home')
@route('/dashboard')
# @view('dashboard')
def dashboard():
    return template('dashboard')


@route('/analysis')
# @view('analysis')
def analysis():
    return template('analysis')


@route('/integrations')
# @view('integrations')
def integrations():
    return template('integrations')


@route('/metadata')
def metadata():
    rows_count = get_rows_count()
    return template('metadata', rows_count=rows_count)


@error(404)
def error404(error):
    return template('404')


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True, reloader=True)
