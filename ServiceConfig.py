import apiai
import json
import TextToSpeech
import eel
import os
from dotenv import load_dotenv
load_dotenv()

def textMessage(message):
    # Token API for Dialogflow
    API_KEY = os.getenv('DIALOGFLOW_API')
    request = apiai.ApiAI(API_KEY).text_request()
    # What language will the request be sent
    request.lang = 'en'
    # Dialog Session ID (you need to learn the bot later)
    request.session_id = '260100'
    # We send a request to the AI ​​with a message from the user
    request.query = message
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    # Parse JSON and pull out the answer
    response = ''
    response = responseJson['result']['fulfillment']['speech']
    # If there is an answer from the bot, we give it out,
    # if not - the bot did not understand it
    if response:
        eel.printAgentDom(response)
        TextToSpeech.say(str(response))
    else:
        return 'I do not quite understand you!'

# textMessage("Hello my dear friend")
