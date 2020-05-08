import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:



        consumer_key = "gYNuhpyKCzPV53qeTFI9EQ19p"
        consumer_secret = "lBSlVpc1ncpg3OWHYFL0SulbLkZ9sXS6p1AvJPAZgVcSbkiRta"
        access_token = "1249848851156140032-0JVenb23eqh7sXvFdsGQHm5MxZ70cU"
        access_secret = "iDVjHFOGnJkgI0nBgt2uC1h4lOxLHMom76q9zxxVZ9tuX"
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client