import json

from Spotify import createPlaylist
from twitter import twitterbotMentionsListener, twitterbotAutho


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
    print('Watson Running')

    returnJSON = twitterbotMentionsListener.getMetaTweet(tweetInfo)

    keywords = make_spotify_data(returnJSON)

    print('Watson Complete')

    createPlaylist.createNewPlaylist(tweetInfo, keywords)
    # reply
    twitterbotMentionsListener.sendReply(tweetInfo, api)
    print('Tweeted out playlist')


if __name__ == '__main__':
    while True:
        main()
