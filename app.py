from twitter import twitterbotMentionsListener, twitterbotAutho
from Spotify import createPlaylist
#from watson import twitterWatsonWrapper


def main():
    api = twitterbotAutho.initApi()
    twitterbotMentionsListener.doReply(api)
    tweetInfo = twitterbotMentionsListener.getData(api)
    # spotify

    createPlaylist.createNewPlaylist(tweetInfo)
    # reply
    twitterbotMentionsListener.sendReply(tweetInfo, api)

    '''
    watsonObject = twitterWatsonWrapper.WatsonAPIObject(tweetInfo.getTimeline())
    watsonObject.populateTimelineNLP()
    watsonObject.populateDataSet()
    '''
if __name__ == '__main__':
    main()