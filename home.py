from sentiment import sentiment_analyzer
from negative import func_neg 
from positive import func_pos
from neutral import func_neutral
from app import text2speech, speech2text
from aylienapiclient import textapi
import time
from aylienapiclient import textapi

client = textapi.Client("TEXTAPI KEY", "TEXTAPI VALUE")

def mains():
	sen = "Hi I am Bozo, your virtual therapist. How are you feeling?"+"\n"
	text2speech(sen)

	query= speech2text()

	a=sentiment_analyzer(query)
	sen2 = "May I know the reason why?"
	text2speech(sen2)

	query2 = speech2text()

	if(a>=0.5):
		func_pos()
	elif(0<=a<0.5):
		func_neutral()
	else:
		func_neg()

	sen3 = "How are you feeling now mate?"
	text2speech(sen3)
	query = speech2text()

	sentiment = client.Sentiment({'text': query})
	lev = 0
	if(sentiment['polarity']=='negative'):
		lev = -1*sentiment['polarity_confidence']
	else:
		lev = sentiment['polarity_confidence']

	if(lev>0.6):
		return
	else:
		time.sleep(30)
	mains()

mains()



