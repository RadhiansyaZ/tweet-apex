import os
import json
import tweepy
from datetime import datetime,timedelta
import pytz

# Options
PRODUCTION = os.environ.get('TWITTER_API_KEY') is not None
if not PRODUCTION :
    from dotenv import load_dotenv
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
    return tweets

def delete_tweet_before_date(tweetObj,date_inp,exception_twt=[]):
    deleted_soon = list()
    cutoff_date = datetime.strptime(date_inp,"%d/%m/%y %H:%M")
    # cutoff_date is still naive, convert it to aware with UTC localization.
    cutoff_date = pytz.utc.localize(cutoff_date)
    # if tweed.created_at < cutoff_date, append the tweet id to list.
    for tweet in tweetObj:
        tweetInfo = tweet['tweet']
        tweetDate = datetime.strptime(tweetInfo['created_at'],"%a %b %d %H:%M:%S %z %Y")
        if tweetDate < cutoff_date and (tweetInfo['id'] not in exception_twt):
            deleted_soon.append(tweetInfo['id'])
    # confimation input in cli and loop thorugh all the id to delete it
    if (input("THIS PROCESS CANNOT BE UNDONE, PROCEED? (Y/N) ").lower() == "y"):
        for tweetID in deleted_soon:
            api.destroy_status(tweetID)
    # print(deleted_soon)
    print("{} tweets was deleted.".format(len(deleted_soon)))

if __name__ == "__main__":
    api = oauth_login(api_key,api_secret)
    print("Authenticated as @{}".format(api.me().screen_name))
    tweets = fetch_tweet_json('tweet.json')
    # date_of_tweet = input("Enter the cutoff date: (DD/MM/YY HH:MM")
    delete_tweet_before_date(tweets, "01/01/13 00:00")