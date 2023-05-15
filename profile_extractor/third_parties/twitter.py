import os
from datetime import datetime, timezone
import logging
import tweepy
from dotenv import (
    load_dotenv,
    find_dotenv,
)  # These imports are used to find .env file and load them the OS

load_dotenv(find_dotenv())

logger = logging.getLogger("twitter")

# Handle Authentication
auth = tweepy.OAuthHandler(
    os.environ.get("TWITTER_API_KEY"), os.environ.get("TWITTER_API_SECRET")
)

auth.set_access_token(
    os.environ.get("TWITTER_ACCESS_TOKEN"), os.environ.get("TWITTER_ACCESS_SECRET")
)

api = tweepy.API(auth)


""" 
Scrape's a twitter user's original tweets (i.e. not retweets or replies) and return them as a dictionaries.
Each dictionaries has 3 fields: "time_posted" (relative to now), "text", "url"
"""


def scrape_user_tweets(username, num_tweets=5):
    tweets = api.user_timeline(screen_name=username, count=num_tweets)
    tweet_list = []

    for tweet in tweets:
        if "RT @" not in tweet.text and not tweet.text.startswith("@"):
            tweet_dict = {}
            tweet_dict["time_posted"] = str(
                datetime.now(timezone.utc) - tweet.created_at
            )
            tweet_dict["text"] = tweet.text
            tweet_dict["url"] = f"https://api.twitter.com/2/users/{tweet.id}/tweets"
            tweet_list.append(tweet_dict)
    return tweet_list
