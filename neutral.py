from api_ai import fetch_reply
from app import text2speech, speech2text
from api_ai import fetch_reply

def func_neutral():
	released = {
	"joke" : "Teacher: Agar koi moti ladki palat ke waapis aae to,is sentence ko English mein kya kahenge?Pappu: Gol Maal Returns!,",
	"video" : "https://www.youtube.com/watch?v=AtkjageFeiY&t=26s" ,
	"meme" : "https://in.pinterest.com/pin/370210031852411340/",
	"surprise" : "https://in.pinterest.com/pin/467741111278425295/",
	"quote" : "Our entire life consists ultimately in accepting ourselves as we are"
	}

	text2speech("Bozo will make sure that your mood gets better"+"\n")

	text2speech(
		"Here's the list which Bozo has incurated specially for you."+"\n"+
		"A funny joke or"+"\n"+
		"A hilarious video from TVF that might lighten your mood Or"+"\n"+
		"A nice meme only for you Or"+"\n"+
		"An inspirational quote Or"+"\n"+
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
