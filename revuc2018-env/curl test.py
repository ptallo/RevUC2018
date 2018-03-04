import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, EmotionOptions
'''pip install --upgrade watson-developer-cloud'''
natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='aa518a49-7b68-4e96-a208-e82fe33784d1',
  password='tOC1RWTjAm0v',
  version='2017-02-27')

response = natural_language_understanding.analyze(
  text='Rumor had it Thratia didn’t appreciate the spidery arm of Valathean law meddling with the Scorched settlements, which meant Ripka was in the shit if Thratia took over. Even with the whole of the Darkling Sea between Valathea’s island empire and the Scorched, the empire’s control over its frontier cities was absolute through its selium-lifted airships and its watchers. The watchers held to imperial law, and kept the Scorched’s selium mines producing to fill Valathean needs and Valathean coffers. And Thratia didn’t much care for Valathean needs, now that they’d kicked her loose. He stifled another oh , watching the honorable watch captain through enlightened eyes. The way she kept glancing at the door, as if she were worried someone would barge in. The way she held her knife, point-out and ready to dance. She was scared senseless.',
  features=Features(
      sentiment=SentimentOptions(),
      emotion=EmotionOptions()))

print(json.dumps(response, indent=2))
