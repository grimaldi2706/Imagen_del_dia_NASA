
#API_KEY: 9rjay2bsKrWMw36aSjpzdq2vw
#API_KEY_SECRET: cWRwEUrGWFYQetYM3RndkJwXm5Vu5A99IoOJgmz2K3uLzf0nHI
#ACCESS_TOKEN: 172901319-SncSVYA82DZZS9DYvipTmz5WyjGemH9suiNzbKbP
#ACCESS_TOKEN_SECRET: vj87yGr5b7gW7u0nhYROM83xtU3Ev0zaIFOLcpr6Cqao6

import tweepy

consumer_key = "9rjay2bsKrWMw36aSjpzdq2vw"
consumer_secret = "cWRwEUrGWFYQetYM3RndkJwXm5Vu5A99IoOJgmz2K3uLzf0nHI"
key = "172901319-SncSVYA82DZZS9DYvipTmz5WyjGemH9suiNzbKbP"
secret = "vj87yGr5b7gW7u0nhYROM83xtU3Ev0zaIFOLcpr6Cqao6"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#api.update_status("This Tweet was Tweeted using Tweepy")

#def tweet(mensaje): 
#    return api.update_status("This Tweet was Tweeted using Tweepy 2")


#filename = open('day.jpg','wb')
 # Definimos la variable de subida de la imagen que vamos a utilizar
#media = api.media_upload('./day.jpg')

    # Definimos cual es el texto que va a utilzar el tweet como status
#tweet = "asdas"

    # Posteamos el tweet con la imagen
#post_result = api.update_status(status=tweet, media_ids=[media.media_id])

#api.update_status("This Tweet was Tweeted using Tweepy",filename)

def tweet(mensaje): 
    api.update_status(mensaje,media_ids=[ret.media_id_string]) 
    return "enviado"