#!/usr/bin/python3
# -*- coding: utf-8 -*-


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Repos(Base):
    __tablename__ = 'repositories'
    id = Column(String(25))
    name_ = Column(String(250))
    full_name = Column(String(250))
    description = Column(String(250))
    homepage = Column(String(250))
    git_url = Column(String(250))
    ssh_url = Column(String(250))
    language_ = Column(String(25))
    private = Column(String(5))
    archived = Column(String(5))
    forks_count = Column(Integer)
    open_issues_count = Column(Integer)
    score = Column(Integer)
    size_ = Column(Integer)
    stargazers_count = Column(Integer)
    watchers_count = Column(Integer)

    def __repr__(self):
        return "<Repos('%d', '%s')>" % (self.id, self.name_)
