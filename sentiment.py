from aylienapiclient import textapi

client = textapi.Client("TEXTAPI KEY", "TEXTAPI VALUE")

def sentiment_analyzer(query):
	sentiment = client.Sentiment({'text': query})
	if(sentiment['polarity']=='negative'):
		return -1*sentiment['polarity_confidence']
	else:
		return sentiment['polarity_confidence'] 
