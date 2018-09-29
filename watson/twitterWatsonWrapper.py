import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, EmotionOptions


# Command for Watson Lib : pip install --upgrade watson-developer-cloud

class WatsonAPIObject:
    def __init__(self, stringArrayList):
        self.watsonSubmitData = stringArrayList  # this should be an array where each entry contains a string
        self.watsonReturnData = []  # this is an array where each entry is a json object corresponding to a watson call
        self.dataSet = {}

    def watsonNLPCall(self, callText):
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            username='aa518a49-7b68-4e96-a208-e82fe33784d1',
            password='tOC1RWTjAm0v',
            version='2017-02-27')

        response = natural_language_understanding.analyze(
            text=callText,
            features=Features(
            sentiment=SentimentOptions(),
            emotion=EmotionOptions(),
            keywords=KeywordsOptions()))

        json_response = json.dumps(response, indent=2)

        return json_response

    def populateReturnData(self):
        for text in self.watsonSubmitData:
            watsonJSON = self.watsonNLPCall(text)
            self.watsonReturnData.append(watsonJSON)

    def populateDataSet(self):
        for entry in self.watsonReturnData:
            watsonDict = json.loads(entry)
            emotionDict = watsonDict['emotion']['document'][
                'emotion']  # the emotion data for a certain watson json object
            for key in emotionDict.keys():
                try:
                    self.dataSet[key]  # testing to see if the key already exists in the dataset
                except KeyError:
                    self.dataSet[key] = []
                finally:
                    self.dataSet[key].append(emotionDict[key])
        print(self.dataSet)
