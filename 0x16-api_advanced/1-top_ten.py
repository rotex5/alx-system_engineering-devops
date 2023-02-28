#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ Request top 10 topics in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64)\
            AppleWebKit/537.36 (KHTML, like Gecko)'

    headers = {'User-Agent': user_agent}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get("data").get("children")
        if len(posts) > 0:
            for post in posts:
                print(post.get("data").get("title"))
        else:
            print(None)
    else:
        print(None)
