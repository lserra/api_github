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
import requests

from repos.db import (
    truncate_tables, get_repos, add_repos, get_rows_count
    )


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
        items = r.json()['items']
        if items is not None:
            truncate_tables()
            add_repos(items)

            parameters = {
                'class_msg': 'success'.upper(),
                'type_msg': 'success',
                'msg': 'The connection to GitHub has been done successfully!',
                'num_repos': get_rows_count(),
                'items': get_repos()
            }
    else:
        parameters = {
            'class_msg': 'warning'.upper(),
            'type_msg': 'warning',
            'msg': 'The connection to GitHub has been done successfully!',
            'items': None
        }

    return parameters


if __name__ == "__main__":
    search_api_github('airflow')
