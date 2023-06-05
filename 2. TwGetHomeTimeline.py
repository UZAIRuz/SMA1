# Chap02/twitter_get_home_timeline.py
import json
from tweepy import Cursor
from twitter1 import get_twitter_client

if __name__ == '__main__':

    client = get_twitter_client()

    with open('jazz_timeline.jsonl', 'w') as f:
        for page in Cursor(client.home_timeline, count = 200).pages(4):
            for status in page:
                # Process a single status
                f.write(json.dumps(status._json)+"\n")
