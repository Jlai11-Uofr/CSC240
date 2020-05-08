import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    try:



        consumer_key = "yM04BiPisVVT1kdlWXHYyXOjM"
        consumer_secret = "gWjUj2JzVXp4n7EUHB8Yh7C1RwJkswM3DxLHk4HYdzMfUHiuwX"
        access_token = "736688330763567104-jfV3sNhYONIdZYpbVY16WpQ39gh9CkI"
        access_secret = "CS9d81JV0paL3ToXaufb9Z583I2yx0MuGIfMTY6Hw97A1"
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