import tweepy

consumer_key = ""
consumer_secret = ""
key = ""
secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

def tweet(mensaje): 
    api.update_status(mensaje,media_ids=[ret.media_id_string]) 
    return "enviado"
