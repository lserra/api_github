#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
API GitHub
Search for all the repositories in the GitHub and storing all the data into a
SQLite database.
================================================================================
Tasks:
1-Capture the keyword and pass to the function 'search_api_github' as parameter
2-Return all repositories has been found and save the results into the database
3-Show all repositories has been found
"""
import sys
import os
import requests
import psycopg2 as db

# setting the parameters
con = None
connection_parameters = {
    'host': os.environ.get('PGHOST'),
    'database': os.environ.get('PGDATABASE'),
    'user': os.environ.get('PGUSER'),
    'password': os.environ.get('PGPASSWORD')
}


def truncate_tables():
    try:
        con = db.connect(
            **connection_parameters
            )

        sql = '''DELETE FROM repositories;'''

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

    except db.DatabaseError as e:
        con.rollback

    finally:
        if con is not None:
            con.close()


def insert_sql_template(item):
    return '''INSERT INTO repositories (id, name_, full_name, description,
    homepage, git_url, ssh_url, language_, private,archived,
    forks_count, open_issues_count, score, size_, stargazers_count,
    watchers_count) VALUES (%(id)s, %(name_)s, %(full_name)s, %(description)s,
    %(homepage)s, %(git_url)s, %(ssh_url)s, %(language_)s, %(private)s,
    %(archived)s, %(forks_count)s, %(open_issues_count)s, %(score)s,
    %(size_)s, %(stargazers_count)s, %(watchers_count)s);
    '''


def insert_repos(items):
    try:
        con = db.connect(
            **connection_parameters
            )
        cur = con.cursor()

        for item in items:
            sql = insert_sql_template(item)
            cur.execute(sql, {
                'id': item.get('id'),
                'name_': item.get('name'),
                'full_name': item.get('full_name'),
                'description': str(item.get('description')).replace('"', ''),
                'homepage': item.get('homepage'),
                'git_url': item.get('git_url'),
                'ssh_url': item.get('ssh_url'),
                'language_': item.get('language'),
                'private': item.get('private'),
                'archived': item.get('archived'),
                'forks_count': int(item.get('forks_count')),
                'open_issues_count': int(item.get('open_issues_count')),
                'score': int(item.get('score')),
                'size_': int(item.get('size')),
                'stargazers_count': int(item.get('stargazers_count')),
                'watchers_count': int(item.get('watchers_count'))
            })

        con.commit()

    except db.DatabaseError as e:
        con.rollback

    finally:
        if con is not None:
            con.close()


def select_sql_template():
    return '''
    SELECT id, name, homepage, git_url, language FROM repositories;
    '''


def select_items():
    try:
        con = db.connect(
            **connection_parameters
            )
        cur = con.cursor()

        sql = select_sql_template()
        cur.execute(sql)

    except db.DatabaseError as e:
        con.rollback

    finally:
        if con is not None:
            con.close()


def search_api_github(name_repo):
    api_url_base = 'https://api.github.com/'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Python Student',
        'Accept': 'application/vnd.github.v3+json'
        }
    api_url = '{}search/repositories?q={}+ \
    language:py&sort=stars&order=desc'.format(api_url_base, name_repo)

    r = requests.get(api_url, headers=headers)

    if r.status_code == 200:
        # TODO: improve this part of the code
        repo_list = r.json()
        items = repo_list['items']
        if items is not None:
            truncate_tables()
            insert_repos(items)
            items = select_items()
            print(items)
            num_repos = len(items)
            type_msg = 'success'
            msg = 'The connection to GitHub has been done successfully!'
    else:
        items = None
        num_repos = 0
        type_msg = 'warning'
        msg = 'The connection to GitHub has not been done successfully!'

    parameters = {
        'class_msg': type_msg.upper(),
        'type_msg': type_msg,
        'msg': msg,
        'num_repos': num_repos,
        'items': items
    }

    return parameters
