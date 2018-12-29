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
import sys
import requests
import sqlite3 as db


def insert_sql_template(item):
    description = str(item.get('description')).replace('"', '')

    return """INSERT INTO repositories ('id','name','full_name','description', \
    'homepage','git_url','ssh_url','language','private','archived', \
    'forks_count', 'open_issues_count', 'score', 'size', 'stargazers_count', \
    'watchers_count') VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}", \
    "{}","{}","{}","{}","{}","{}","{}")
    """.format(
        item.get('id'), item.get('name'), item.get('full_name'),
        description, item.get('homepage'), item.get('git_url'),
        item.get('ssh_url'), item.get('language'), item.get('private'),
        item.get('archived'), int(item.get('forks_count')),
        int(item.get('open_issues_count')), int(item.get('score')),
        int(item.get('size')), int(item.get('stargazers_count')),
        int(item.get('watchers_count'))
        )


def insert_repos(items):
    con = None

    try:
        con = db.connect(
            '/home/lserra/PycharmProjects/api_github/data/github.db'
            )

        cur = con.cursor()

        for item in items:
            sql = insert_sql_template(item)
            cur.execute(sql)

        con.commit()

        print(">> Total rows inserted: {}\n".format(len(items)))

    except db.DatabaseError as e:
        print(">> Error %s: " % e.args[0])
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
        insert_repos(items)
    else:
        print('>> No Repo List Found\n')
