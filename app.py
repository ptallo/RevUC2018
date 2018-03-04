from twitter import twitterbotMentionsListener, twitterbotAutho
from Spotify import createPlaylist
from watson import twitterWatsonWrapper
import json

def makeSpotifyData(watsonJSON):
    watsonDict = json.loads(watsonJSON)
    keywords = watsonDict['keywords']
    keywords_array = []
    for dict in keywords:
        keywords_array.append(dict['text'])
    return keywords_array

def main():
    api = twitterbotAutho.initApi()
    twitterbotMentionsListener.doReply(api)
    tweetInfo = twitterbotMentionsListener.getData(api)
    # spotify
    print(tweetInfo.getTimeline()[0])

    metaTweet = ""
    for tweet in tweetInfo.getTimeline():
        metaTweet += (" " + tweet) if len(metaTweet)==0 else tweet
    watsonObject = twitterWatsonWrapper.WatsonAPIObject(tweetInfo.getTimeline())
    returnJSON = watsonObject.watsonNLPCall(metaTweet)

    keywords = makeSpotifyData(returnJSON)

    createPlaylist.createNewPlaylist(tweetInfo, keywords)
    # reply
    twitterbotMentionsListener.sendReply(tweetInfo, api)

if __name__ == '__main__':
    while True:
        main()


