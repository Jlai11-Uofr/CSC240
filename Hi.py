import sys
import json
import os
import tweepy
from tweepy import Cursor
import progressbar
import datetime
import time


import client1
import client2



from tqdm import tqdm
start_date = datetime.datetime(2020, 1, 20, 0, 0, 0)
end_date = datetime.datetime(2020, 4, 14, 23, 59, 59)

def get_tweets(userid, api, output_dir):
    print("Getting <{}> tweets".format(userid))
    output_file = "{}_tweets.jsonl".format(userid)
    print(output_file)
    if output_file in os.listdir(output_dir):
        print('Skip!')
    else:
        count = 0
        with progressbar.ProgressBar(max_value=progressbar.UnknownLength) as bar:
            tweets = []
            try:
                tmp_tweets = api.user_timeline(user_id=userid, count=200)

                for tweet in tmp_tweets:

                        tweets.append(tweet)
                        count += 1
                        bar.update(count)

                if tweets:
                    last_tweet = None
                    while tmp_tweets[-1].created_at > start_date and tmp_tweets[-1] != last_tweet:
                        print("\nLast tweet @", tmp_tweets[-1].created_at, " - Fetch more ...")
                        tmp_tweets = api.user_timeline(user_id=userid, count=200)
                        last_tweet = tmp_tweets[-1]
                        print(last_tweet.text)

                        for tweet in tmp_tweets:
                            if tweet.created_at < end_date and tweet.created_at > start_date:
                                tweets.append(tweet)
                                count += 1
                                bar.update(count)
                    with open(output_dir+'/'+output_file, 'w') as f:
                        for tweet in tweets:
                            f.write(json.dumps(tweet._json)+"\n")
            except tweepy.TweepError as e:
                print(e)

                pass
directory = os.getcwd()
output_dir = directory+'/user-timelines' ##Where images are donwloaded

text_file = open("NewData.txt", "r")  ##input file
users = text_file.readlines()
p = 1%9

for i in tqdm(range(0,len(users))):
    x = i%2
    if x == 1:
        api = client1.get_twitter_client()
        get_tweets(users[i],api,output_dir)
    else:
        api = client2.get_twitter_client()
        get_tweets(users[i], api, output_dir)

3430882365

