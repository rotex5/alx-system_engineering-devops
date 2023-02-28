#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for
a given subreddit. If an invalid subreddit is given,
the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """ Request for a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64)\
            AppleWebKit/537.36 (KHTML, like Gecko)'

    headers = {
        'User-Agent': user_agent
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
