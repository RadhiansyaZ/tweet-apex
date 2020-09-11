import os
from dotenv import load_dotenv
import tweepy
from datetime import datetime,timedelta

# Options
PRODUCTION = os.environ.get('TWITTER_API_KEY') is not None

if not PRODUCTION :
    load_dotenv(override=True)

api_key = os.environ.get('TWITTER_API_KEY')
api_secret = os.environ.get('TWT_API_SECRET')
access_token = os.environ.get('ACESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')


if __name__ == "__main__":
    pass