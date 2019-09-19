#!/usr/bin/python3
"""Get request to reddit API"""
import requests


def top_ten(subreddit):
    """Get request"""
    base_url = 'https://www.reddit.com/r/{}/top/.json'.format(subreddit)
    h = {'User-Agent': 'Reddit API test'}
    params = {'limit': 10}
    r = requests.get(base_url, headers=h, allow_redirects=False, params=params)
    d = r.json()
    if d.get('error', 200) == 404:
        print(None)
        return
    l = d.get('data').get('children')
    for dic in l[:10]:
        print(dic.get('data').get('title'))
