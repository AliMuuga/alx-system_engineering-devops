#!/usr/bin/python3
"""Query Reddit API to get the number of subscribers for a given subreddit"""

import requests

def number_of_subscribers(subreddit):
    """Fetches the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    headers = {'User-Agent': 'my_reddit_app/0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0

