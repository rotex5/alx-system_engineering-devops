#!/usr/bin/python3
"""
recursive function that queries the Reddit API
If no results are found for the given
subreddit, skip and do not print it.
"""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """
    GET the word count for each word in word_list.
    Print results in descending order by the count, not the title.
    If no posts match or subreddit is invalid, print a newline.
    If a word has no matches, skip and do not print it.
    """
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64)\
            AppleWebKit/537.36 (KHTML, like Gecko)'
    header = {'User-Agent': user_agent}

    if counts is None:
        counts = {}

    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
                                                            subreddit, after)

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")
    after = data.get("after")
    children = data.get("children")

    for child in children:
        title = child.get("data").get("title")
        words = title.lower().split()
        for word in word_list:
            if word.lower() in words:
                if word.lower() in counts:
                    counts[word.lower()] += words.count(word.lower())
                else:
                    counts[word.lower()] = words.count(word.lower())

    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for count in sorted_counts:
            print("{}: {}".format(count[0], count[1]))
    else:
        return count_words(subreddit, word_list, counts, after)
