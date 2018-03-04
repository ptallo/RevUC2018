import tweepy

import twitterbotAutho
import json

def get(self):

    # return mentions
    mentions = self.mentions_timeline(count=1)

    readableJson = json.dumps(mentions[0]._json)

    loadedJson = json.loads(readableJson)



if __name__ == '__main__':
    api = twitterbotAutho.initApi()
    api.replyToMentions()


