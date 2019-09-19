#!/usr/bin/python3
"""Get request to reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=1):
    """Recursive function"""
    base_url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    h = {'User-Agent': 'Reddit API test'}
    params = {'limit': 200, 'after': after}
    r = requests.get(base_url, headers=h, allow_redirects=False, params=params)
    d = r.json()
    if d.get('error', 200) == 404:
        return None
    if after is None:
        return hot_list
    l = d.get('data').get('children')
    for dic in l:
        hot_list.append(dic.get('data').get('title'))
    p = d.get('data').get('after')
    return recurse(subreddit, hot_list, p)
