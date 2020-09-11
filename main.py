import os
import tweepy
import requests
import json
from dotenv import load_dotenv
from datetime import datetime,timedelta

# Options
PRODUCTION = os.environ.get('TWITTER_API_KEY') is not None
if not PRODUCTION :
    load_dotenv(override=True)

api_key = os.environ.get('TWITTER_API_KEY')
api_secret = os.environ.get('TWT_API_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

# Function
def oauth_login(api_key, api_secret):
    auth = tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication ok!")
    except:
        print("Error when Authenticating")
    return api

def oauth2_login(api_key, api_secret):
    auth = tweepy.AppAuthHandler(api_key,api_secret)
    return tweepy.API(auth)

def fetch_tweet_json(filename):
    with open(filename,encoding='utf8') as f:
        tweets = json.load(f)
    print(tweets) # Debug line
    return tweets

def delete_tweet_before_date(tweetObj,date):
    deleted_soon = list()
    # if date < date local var, append the tweet id to list
    # confimation input in cli
    # loop thorugh all the id to delete it
    pass

if __name__ == "__main__":
    api = oauth_login(api_key,api_secret)
    print("Authenticated as @{}".format(api.me().screen_name))
    # api = oauth2_login(api_key,api_secret)
    tweets = fetch_tweet_json('tweet.json')