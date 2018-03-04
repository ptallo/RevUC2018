import tweepy
import json
import twitterbotMentionsListener, twitterbotAutho, TweetData
from random import *

# Sends the reply
def sendReply(TweetData, api):
    SimpleResponses = ['Rock on! ', 'Enjoy! ', 'Just for you! ', 'Have a listen! ']
    response = SimpleResponses[randint(0, 3)]
    response += TweetData.getPlayListLink()
    response += '@'
    response += TweetData.getUserName()
    TweetData.setTweetReplyText(response)
    api.update_status(TweetData.getTweetReplyText(), in_reply_to_status_id=TweetData.getStatusID())
