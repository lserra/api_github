#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
API GitHub
Search for all the repositories in the GitHub and storing all the data into a
SQLite database.

This task should be run daily through a cronjob to check for new tips and
update the stats (number of likes and retweets) on existing tweets.
The tables are recreated daily.
"""
# TODO: logging all tasks
# TODO: truncate tables

import sys
import os
import requests
import psycopg2 as db


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

        print(">> Table has been truncated\n")

    except db.DatabaseError as e:
        print(">> Error %s: " % e.args[0])
        con.rollback
        sys.exit(1)

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

        print(">> Total rows inserted: {}\n".format(len(items)))

    except db.DatabaseError as e:
        print(">> Error %s: " % e.args[0])
        con.rollback
        sys.exit(1)

    finally:
        if con is not None:
            con.close()


def get_repos(name_repo):
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
        print("STATUS: Connection OK!\n")
    else:
        print("STATUS: Connection NOK. Error: {}\n".format(r.text))

    return r.json()


if __name__ == '__main__':
    repo_list = get_repos('airflow')
    items = repo_list['items']

    if items is not None:
        truncate_tables()
        insert_repos(items)
    else:
        print('>> No Repo List Found\n')
