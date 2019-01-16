#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
# from tips.db import get_hashtags, get_tips
from bottle import (
    default_app, route, run, request, static_file, view, template, error
    )
from repos.db import get_rows_count
from tasks.integrations import search_api_github


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
@view('integrations')
def integrations():
    return dict(
        type_msg=None,
        items=None
        )


@route('/search', method='POST')
def search():
    keyword = request.request.forms.get('keyword')

    if keyword is not None:
        parameters = search_api_github(keyword)

        class_msg = parameters.get('class_msg')
        type_msg = parameters.get('type_msg')
        msg = parameters.get('msg')
        num_repos = parameters.get('num_repos')
        items = parameters.get('items')

    return template(
        'integrations',
        class_msg=class_msg,
        type_msg=type_msg,
        msg=msg,
        num_repos=num_pos,
        items=items)


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
