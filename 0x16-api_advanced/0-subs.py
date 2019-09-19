#!/usr/bin/python3
"""Get request to reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Get request"""
    base_url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    h = {'User-Agent': 'Reddit API test'}
    print(base_url)
    r = requests.get(base_url, headers=h, allow_redirects=False)
    d = r.json()
    if d.get('error', 200) == 404:
        return 0
    return d.get('data').get('children')[0]\
                        .get('data').get('subreddit_subscribers')
