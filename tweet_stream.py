import tweepy
import re
import validators
import secret

def clean(tweet):
    tweet = tweet.lower()
    
    words = []
    for word in tweet.split(' '):
        if not validators.url(word) and word != "rt" and word != " ":
            words.append(word.strip())

    tweet = " ".join(words)

    for char in tweet:
        if char in "+-/.,!?()[]':1234567890":
            tweet = tweet.replace(char, '')
    words = []
    for word in tweet.split(' '):
        isValid = True
        for char in word:
            if char not in "abcdefghijklmnopqrstuvwxyz":
                isValid = False
                break
        if isValid:
            words.append(word.strip())
    return " ".join(words)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        f = open('tweets.txt', 'a')
        cleaned = clean(status.text)
        f.write(cleaned + "\n")
        print(cleaned)

consumer_key = secret.consumer_key
consumer_secret = secret.consumer_secret

access_token = secret.access_token
access_secret = secret.access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)



myStream.filter(track=['is', 'a', 'the'], languages=['en'])

