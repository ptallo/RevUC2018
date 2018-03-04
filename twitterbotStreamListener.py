import tweepy

import twitterbotAutho
import json

api = twitterbotAutho.initApi()

mentions = api.mentions_timeline()

print(mentions)



