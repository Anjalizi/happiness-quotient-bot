from api_ai import fetch_reply
from app import text2speech, speech2text

# print("Bozo is here for you. I can help you by telling:"+"\n")

def func_pos():
	released = {
	"song" : "https://www.youtube.com/watch?v=0gosur3db5I&list=RD0gosur3db5I",
	"tv show" : "https://www.youtube.com/watch?v=AtkjageFeiY&t=26s" ,
	"meme" : "https://in.pinterest.com/pin/370210031852411340/",
	"surprise" : "https://in.pinterest.com/pin/467741111278425295/"
	}

	text2speech("Glad to hear that"+"\n")
	text2speech(
		"Here's the list which Bozo has incurated specially for you."+"\n"+
		"A rocking song or"+"\n"+
		"One of your favourite Netflix series or"+"\n"+
		"A nice meme or"+"\n"+
		"A surprise!"+"\n\n"+
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
