import apiai
import json
import requests

APIAI_ACCESS_TOKEN = "APIAI_ACCESS_TOKEN"

ai = apiai.ApiAI(APIAI_ACCESS_TOKEN)

def apiai_response(query, session_id):
	"""
	function to fetch api.ai response
	"""
	request = ai.text_request()
	request.lang='en'
	request.session_id=session_id
	request.query = query
	response = request.getresponse()
	return json.loads(response.read().decode('utf8'))

def fetch_reply(query, session_id):
	"""
	main function to fetch reply for chatbot and 
	return a reply dict with reply 'type' and 'data'
	"""
	response = apiai_response(query, session_id)
	if (len( response['result']['parameters'])==0):
		return "none"
	return response['result']['parameters']['happy_list'];
