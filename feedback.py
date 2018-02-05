from aylienapiclient import textapi
import time
from home import mains

client = textapi.Client("TEXTAPI KEY", "TEXTAPI VALUE")

def feedback_analyzer(query):
	sentiment = client.Sentiment({'text': query})
	lev = 0
	if(sentiment['polarity']=='negative'):
		lev = -1*sentiment['polarity_confidence']
	else:
		lev = sentiment['polarity_confidence']

	if(lev>0.6):
		return
	else:
		time.sleep(3600)
	mains()


