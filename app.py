"""
### API GitHub
Realiza pesquisa de repositorios no GitHub e armazena estas informaçoes no BD (SQLite)
"""
import sys
import requests
import sqlite3 as db

api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'Python Student',
           'Accept': 'application/vnd.github.v3+json'}


def insert_sql_template(item):
    return """
    INSERT INTO repositories ('id','name','full_name','description','homepage','git_url','ssh_url','language','private',
    'archived') VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
    """.format(item.get('id'), item.get('name'), item.get('full_name'), item.get('description'), item.get('homepage'),
               item.get('git_url'), item.get('ssh_url'), item.get('language'), item.get('private'),
               item.get('archived')
               )


def insert_repos(items):
    con = None

    try:
        con = db.connect('/home/lserra/PycharmProjects/api_github/data/github.db')

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
    api_url = '{}search/repositories?q={}+language:py&sort=stars&order=desc'.format(api_url_base, name_repo)

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
