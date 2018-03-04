import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, EmotionOptions
'''pip install --upgrade watson-developer-cloud'''

def watsonNLPCall(apiText):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
      username='aa518a49-7b68-4e96-a208-e82fe33784d1',
      password='tOC1RWTjAm0v',
      version='2017-02-27')

    response = natural_language_understanding.analyze(
      text=apiText,
      features=Features(
          sentiment=SentimentOptions(),
          emotion=EmotionOptions()))

    json_response = json.dumps(response, indent=2)

    return json_response


