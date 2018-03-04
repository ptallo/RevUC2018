from watson import watsonCall


class WatsonDataWrapper:
    def __init__(self, tweetData):
        self.tweetData = tweetData
        self.timelineNLP = []

    def populateTimelineNLP(self):
        for tweetText in self.tweetData.getTimeline():
            tweetJSON = watsonCall.watsonNLPCall(tweetText)
            self.timelineNLP.append(tweetJSON)




