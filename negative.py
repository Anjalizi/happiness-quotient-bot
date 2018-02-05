from api_ai import fetch_reply
from app import text2speech, speech2text

def func_neg():
	released = {
	"joke" : "Mayank",
	"video" : "https://www.youtube.com/watch?v=AtkjageFeiY&t=26s" ,
	"meme" : "https://in.pinterest.com/pin/370210031852411340/",
	"surprise" : "https://in.pinterest.com/pin/467741111278425295/"
	}

	text2speech("Sorry to hear that. But don't worry Bozo is here to uplift your mood")

	text2speech(
		"Here's the list which Bozo has incurated specially for you."+"\n"+
		"A hilarious joke or"+"\n"+
		"A hilarious video from TVF that might lighten your mood or"+"\n"+
		"A nice meme or"+"\n"+
		"Or a surprise!"+"\n\n"+
		"What do you want to hear?"
		)

	query = speech2text()
	
	for i in range(0,5):
		response = fetch_reply(query,1)
		if(response!="none"):
			print(response)
			text2speech("Here is an awesome " + response + " for you: " + released[response])
			return
		else:
			print("I couldn't understand that. Please say that again for me.")
			query = speech2text()
