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
import logging
import os
import sys

import psycopg2 as db
import requests

# setting the parameters
con = None
connection_parameters = {
    'host': os.environ.get('PGHOST'),
    'database': os.environ.get('PGDATABASE'),
    'user': os.environ.get('PGUSER'),
    'password': os.environ.get('PGPASSWORD')
}

# create logger
logger = logging.getLogger('task_etl')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def truncate_tables():
    global con
    try:
        con = db.connect(
            **connection_parameters
            )

        sql = '''DELETE FROM repositories;'''

        logger.info('Opening the connection to the database')
        cur = con.cursor()
        logger.info('Truncating the table')
        cur.execute(sql)
        print(">> Table has been truncated\n")
        logger.info('Committing all the data into the database')
        con.commit()

    except db.DatabaseError as e:
        print(">> Something wrong!\n")

        logger.error('%s', e.args[0])
        logger.warning('Doing the rollback')
        con.rollback
        sys.exit(1)

    finally:
        if con is not None:
            logger.info('Closing the connection to the database')
            con.close()


def insert_sql_template():
    return '''INSERT INTO repositories (id, name_, full_name, description,
    homepage, git_url, ssh_url, language_, private,archived,
    forks_count, open_issues_count, score, size_, stargazers_count,
    watchers_count) VALUES (%(id)s, %(name_)s, %(full_name)s, %(description)s,
    %(homepage)s, %(git_url)s, %(ssh_url)s, %(language_)s, %(private)s,
    %(archived)s, %(forks_count)s, %(open_issues_count)s, %(score)s,
    %(size_)s, %(stargazers_count)s, %(watchers_count)s);
    '''


def insert_repos(items):
    global con
    try:
        con = db.connect(
            **connection_parameters
            )
        logger.info('Opening the connection to the database')
        cur = con.cursor()

        for item in items:
            sql = insert_sql_template()

            logger.info('Inserting a new repository in the table')
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

        print(">> Total repositories inserted: {}\n".format(len(items)))
        logger.info('Committing all the data into the database')
        con.commit()

    except db.DatabaseError as e:
        print(">> Something wrong!\n")

        logger.error('%s', e.args[0])
        logger.warning('Doing the rollback')
        con.rollback
        sys.exit(1)

    finally:
        if con is not None:
            logger.info('Closing the connection to the database')
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

    logger.info('Requesting to GitHub and searching for all the repositories')
    r = requests.get(api_url, headers=headers)

    if r.status_code == 200:
        print(">> STATUS: Connection OK!\n")
    else:
        print(">> STATUS: Connection NOK!\n")
        logger.error('%s', r.text)
        sys.exit(1)

    return r.json()


if __name__ == '__main__':
    logger.info('Process started ...')
    repo_list = get_repos('airflow')
    items = repo_list['items']

    if items is not None:
        truncate_tables()
        insert_repos(items)
    else:
        print('>> No Repo List Found\n')

    logger.info('Process finished!')
