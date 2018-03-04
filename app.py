from twitter import twitterbotMentionsListener, twitterbotAutho
from watson import twitterWatsonWrapper


def main():
    api = twitterbotAutho.initApi()
    tweetInfo = twitterbotMentionsListener.getData(api)

    watsonObject = twitterWatsonWrapper.WatsonDataWrapper(tweetInfo)
    watsonObject.populateTimelineNLP()

if __name__ == '__main__':
    main()