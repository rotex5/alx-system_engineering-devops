#!/usr/bin/python3
"""
recursive function that queries the Reddit API
If no results are found for the given
subreddit, skip and do not print it.
"""
import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """
    GET the word count for each word in word_list.
    Print results in descending order by the count, not the title.
    If no posts match or subreddit is invalid, print a newline.
    If a word has no matches, skip and do not print it.
    """
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64)\
            AppleWebKit/537.36 (KHTML, like Gecko)'
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'User-Agent': user_agent}
    params = {
            'limit': 100,
            'after': after
            }

    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot_articles = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot_articles:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dict)
