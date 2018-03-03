import tweepy

consumer_key = 	"0j5zlz4h5IQ71ncz8ZsrpTEMc"
consumer_secret = 	"zJpRVvpMGI13c1MnDrzAKC6fwIIpoUJa25YAFAV4B9aovKDdwe"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text