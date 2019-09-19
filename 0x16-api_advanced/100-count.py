#!/usr/bin/python3
"""Get request to reddit API"""
import re
import requests


def contains(word, title):
    """Checks if words is in title"""
    pat = r"(?i)\s{}\s".format(word)
    if re.search(pat, title):
        return True
    return False


def recurse(subreddit, word_list, after=1, dic={}):
    """Recursive function"""
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': 'Reddit API test'}
    params = {'limit': 200, 'after': after}
    r = requests.get(base_url, headers=h, allow_redirects=False, params=params)
    if r.status_code > 299:
        return None
    d = r.json()
    if after is None:
        return dic
    l = d.get('data').get('children')
    for i in l:
        title = i.get('data').get('title').lower()
        for j in word_list:
            if contains(j, title):
                if j not in dic:
                    dic[j] = 1
#                   #dic[j] = [title]
                else:
                    dic[j] += 1
#                   #dic[j].append(title)
    p = d.get('data').get('after')
    return recurse(subreddit, word_list, p, dic)


def count_words(subreddit, word_list):
    """Cound # of keywords"""
    d = recurse(subreddit, word_list)
    if d:
        for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True):
            print("{}: {}".format(key, value))
#        # import pprint
#       # pp = pprint.PrettyPrinter(indent=4)
#       # pp.pprint(d)
