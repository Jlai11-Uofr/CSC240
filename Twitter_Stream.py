from tweepy.streaming import StreamListener
from tweepy import Stream
import pandas as pd
import tweepy
import csv
import time

def authenticate(Path):
    lol = open(Path,'r')
    global consumer_key
    global consumer_secret
    global access_token
    global access_token_secret
    temp = []
    for line in lol:
        temp.append(line.split(None, 1)[0])

    consumer_key = temp[0]

    consumer_secret = temp[1]

    access_token = temp[2]

    access_token_secret = temp[3]
##Login to Twitter API using Tweepy
authenticate("Passwords.txt")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)







class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        with open("Facemask_data16.csv",'a') as f:
            writer= csv.writer(f)



            try:
                if hasattr(status, 'retweeted_status') and hasattr(status.retweeted_status, 'extended_tweet'):
                    print('retweeted: ' + status.retweeted_status.extended_tweet.full_text.encode('utf-8'))
                   # writer.writerow([status.user.screen_name, str(status.user.id), status.retweeted_status.extended_tweet.full_text.encode('utf-8')])
                if hasattr(status, 'extended_tweet'):
                    print('extended_tweet: ' + status.extended_tweet.full_text.encode('utf-8'))
                    writer.writerow([status.user.screen_name, str(status.id),
                                     status.extended_tweet.full_text.encode('utf-8'),status.user.location.encode('utf-8'),status.place])

                else:
                    writer.writerow([status.user.screen_name, str(status.id),
                                     status.text.encode('utf-8'),status.user.location.encode('utf-8'),status.place])
                    print('text: ' + status.text.encode('utf-8'))
            except AttributeError:
                print('attribute error: ' + status.text)
                writer.writerow([status.user.screen_name, str(status.id),
                                 status.text.encode('utf-8'),status.place])




    def on_error(self, status_code):
        print( 'Encountered error with status code:', status_code)
        time.sleep(200)
        return True

    def on_timeout(self):
        print( 'Timeout...')
        return True


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener,tweet_mode ='extended')

with open("Facemask_data16.csv",'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Username','Id','Tweet','Location','Geo'])

key_terms = ['Facemask','mask',"coronavirus","covid-19"]


myStream.filter(track=key_terms,is_async=True,languages=["en"],encoding='utf-8')
