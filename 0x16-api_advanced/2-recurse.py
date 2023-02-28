#!/usr/bin/python3
"""
recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the given
subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Request all hot articles in a subreddit"""
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64)\
            AppleWebKit/537.36 (KHTML, like Gecko)'

    if (after is None):
        return hot_list

    if (len(hot_list) == 0):
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)

    headers = {'user-agent': user_agent}

    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return None
    elif 'data' not in response.json():
        return None
    else:
        res = response.json()
        for post in res['data']['children']:
            hot_list.append(post['data']['title'])

    after = res['data']['after']
    return recurse(subreddit, hot_list, after)
