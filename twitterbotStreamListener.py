import tweepy

import twitterbotAutho

api = twitterbotAutho.initApi()

status = api.home_timeline()


'''
sampleTweets = ['The richest love is that which submits to the arbitration of time.', 'It is during our darkest moments that we must focus to see the light', 'Music was my refuge. I could crawl into the space between the notes and curl my back to loneliness', 'Every mans work, whether it be literature, or music or pictures or architecture or anything else, is always a portrait of himself.', 'Music is the greatest communication in the world. Even if people do not understand the language that you are singing in, they still know good music when they hear it.']

for x in sampleTweets:
    api.update_status(status=x)
'''

