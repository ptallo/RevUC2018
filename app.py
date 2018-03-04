from twitter import twitterbotMentionsListener, twitterbotAutho
#from watson import twitterWatsonWrapper


def main():
    api = twitterbotAutho.initApi()
    tweetInfo = twitterbotMentionsListener.getData(api)

    twitterbotMentionsListener.doReply(api)

    twitterbotMentionsListener.sendReply(tweetInfo, api)

    '''
    watsonObject = twitterWatsonWrapper.WatsonAPIObject(tweetInfo.getTimeline())
    watsonObject.populateTimelineNLP()
    watsonObject.populateDataSet()
    '''
if __name__ == '__main__':
    main()