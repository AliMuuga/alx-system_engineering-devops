#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if not isinstance(subreddit, str) or not subreddit:
        return 0

    user_agent = {'User-Agent': 'my_reddit_app/0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = get(url, headers=user_agent)

    if response.status_code == 200:
        try:
            results = response.json()
            return results.get('data', {}).get('subscribers', 0)
        except ValueError:
            return 0
    return 0
