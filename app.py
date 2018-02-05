import speech_recognition as sr
import bs4 as bs
import urllib  
from tts_watson.TtsWatson import TtsWatson
import os

ttsWatson = TtsWatson('WATSON KEY', 'WATSON VALUE', 'en-US_AllisonVoice')

def text2speech(query):
	ttsWatson.play(query)

def speech2text():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)
	try:
		print("You said: " + r.recognize_google(audio))
		return r.recognize_google(audio)
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
