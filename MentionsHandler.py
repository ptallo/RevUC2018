import tweepy
import json

# returns usable json object from mentions
def getMention(self):
    mentions = self.mentions_timeline(count=1)

    readableJson = json.dumps(mentions[0]._json)

    return json.loads(readableJson)
