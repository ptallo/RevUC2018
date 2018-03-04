from twitter import TweetData
import json
import time
import datetime
from random import *

def getMention(api):
    mentions = api.mentions_timeline(count=1)

    readableJson = json.dumps(mentions[0]._json)

    return json.loads(readableJson)

# populates data and returns TweetData Object
def getData(api):
    mentions = getMention(api)
    data = TweetData.TweetData()
    data.setStatusId(mentions['id'])
    data.setUserName(mentions['user']['screen_name'])

    # constructs the timeline on data object
    timeline = api.user_timeline(id=mentions['user']['id'], count=100)
    for x in timeline:
        # Creates the dict
        readableJsonTimeline = json.loads(json.dumps(x._json))
        data.addToTimeline(readableJsonTimeline['text'])

    # construct followers
    followerIds = api.friends_ids(id=mentions['user']['id'])
    for id in followerIds:
        user = api.get_user(id)
        readableUser = json.loads(json.dumps(user._json))
        screenName = readableUser['screen_name']
        userName = readableUser['name']
        data.addUserFollower(userName, screenName, id)

    return data


def doReply(api):
    # gather latest tweet and mention
    newestMention = getMention(api)
    newestMentionID = newestMention['id']
    newestTweet = api.home_timeline(count=1)
    newestTweetJson = json.loads(json.dumps(newestTweet[0]._json))
    newestTweetID = newestTweetJson['id']

    # Compare the IDs
    while newestMentionID < newestTweetID:
        time.sleep(30)
        newestMention = getMention(api)
        newestMentionID = newestMention['id']
        print('Waiting...')

    return True


# Sends the reply
def sendReply(TweetData, api):
    SimpleResponses = ['Rock on! ', 'Enjoy! ', 'Just for you! ', 'Have a listen! ']
    response = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    response += SimpleResponses[randint(0, 3)]
    response += TweetData.getPlayListLink()
    response += '@'
    response += TweetData.getUserName()
    TweetData.setTweetReplyText(response)
    print(TweetData.getTweetReplyText())
    api.update_status(TweetData.getTweetReplyText(), in_reply_to_status_id=TweetData.getStatusID())












