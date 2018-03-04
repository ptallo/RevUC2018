class TweetData:

    # Constructor
    def __init__(self):
        self.statusId = 0
        self.userName = ''
        self.playlistLink = ''
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

    # Set playlist link
    def setPlaylistLink(self, link):
        self.playlistLink = link

    # Get playlist link
    def getPlayListLink(self):
        return self.playlistLink

    # Set TweetReply
    def setTweetReplyText(self, newTweetReplyText):
        self.tweetReplyText = newTweetReplyText

    # Get TweetReply
    def getTweetReplyText(self):
        return self.tweetReplyText

    # adds status to timeline
    def addToTimeline(self, status):
        self.userTimeline.append(status)

    # Get list of status
    def getTimeline(self):
        return self.userTimeline

    # set Followers
    def addUserFollower(self, userName, screenName, userID):
        tempDict = {}
        tempDict['screenName'] = screenName
        tempDict['userName'] = userName
        tempDict['userId'] = userID
        self.userFollowers.append(tempDict)

    # Get Followers
    def getUserFollowers(self):
        return self.userFollowers

    def diagnosticPrint(self):
        print(self.statusId)
        print('\n')
        print(self.userName)
        print('\n')
        print(self.tweetReplyText)
        print('\n')
        print(self.userTimeline)
        print('\n')
        print(self.userFollowers)