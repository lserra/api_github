#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
This task should be run in a daily cronjob to look for new tips and update
stats (number of likes and retweets) on existing tweets.
The tables are recreated daily.
"""
from tasks.import_tweets import get_hashtag, get_tweet
from tips.db import (
    truncate_tables, get_hashtags, add_hashtags, get_tips, add_tips
    )


if __name__ == '__main__':
    truncate_tables()
    get_tweet()
    get_hashtag()
