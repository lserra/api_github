#!/usr/bin/python3
# -*- coding: utf-8 -*-


# from os import environ
import sys
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from repos.models import Base, Repos


def _create_session():
    db_url = os.environ.get('DATABASE_URL')

    if 'github' in sys.argv:
        db_url += '_test'

    if not db_url:
        raise EnvironmentError('Need to set the DATABASE_URL parameter')

    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    return create_session()


session = _create_session()


def truncate_tables():
    session.query(Repos).delete()
    session.commit()


def get_repos():
    repos = session.query(
        Repos.id, Repos.name_, Repos.homepage, Repos.git_url, Repos.language_
        )
    repos = repos.order_by(Repos.name_.asc())

    return repos.all()


def add_repos(items):
    for item in items:
        session.add(
            Repos(
                id=item.get('id')
                name_=item.get('name')
                full_name=item.get('full_name'),
                description=str(item.get('description')).replace('"', ''),
                homepage=item.get('homepage'),
                git_url=item.get('git_url'),
                ssh_url=item.get('ssh_url'),
                language_=item.get('language'),
                private=item.get('private'),
                archived=item.get('archived'),
                forks_count=int(item.get('forks_count')),
                open_issues_count=int(item.get('open_issues_count')),
                score=int(item.get('score')),
                size_=int(item.get('size')),
                stargazers_count=int(item.get('stargazers_count')),
                watchers_count=int(item.get('watchers_count'))
                )
            )
    session.commit()


def get_rows_count():
    rows_count = session.query(Repos).count()
    return rows_count
