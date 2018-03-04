import json
import tweepy

class TweetData:

    def __init__(self):
        self.statusId = 0
        self.userName = ''
        self.tweetReplyText = ''
        self.userTimeline = []
        self.userFollowers = []


    # Sets Status ID
    def setStatusId(self, newStatusId):
        self.statusId = newStatusId

    # Gets Status ID
    def getStatusID(self):
        return self.statusId

    # Set UserName
    def setUserName(self, newUserName):
        self.userName = newUserName

    # Get UserName
    def getUserName(self):
        return self.userName

    # Set TweetReply
    def setTweetReplyText(self, newTweetReplyText):
        self.tweetReplyText = newTweetReplyText

    # Get TweetReply
    def getTweetReplyText(self):
        return self.tweetReplyText

    def addUser