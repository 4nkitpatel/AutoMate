import requests
import eel
import TextToSpeech


def find(word):
    url = "https://api.dictionaryapi.dev/api/v1/entries/en/" + word
    res = requests.get(url)
    data = res.json()
    TextToSpeech.say("Here Are some Result For Your Query")
    errFlag = True
    try:
        eel.printAgentDom("Definition : \n" + data[0]['meaning']['exclamation'][0]['definition'])
        errFlag = False
    except KeyError as e:
        pass

    try:
        eel.printAgentDom("Example : \n" + data[0]['meaning']['exclamation'][0]['example'])
        errFlag = False
    except KeyError as e:
        pass

    try:
        eel.printAgentDom("Noun Definition : \n" + data[0]['meaning']['noun'][0]['definition'])
        errFlag = False
    except KeyError as e:
        pass

    try:
        eel.printAgentDom("Noun Example : \n" + data[0]['meaning']['noun'][0]['example'])
        errFlag = False
    except KeyError as e:
        pass

    try:
        eel.printAgentDom("Synonyms : \n" + str(data[0]['meaning']['noun'][0]['synonyms']))
        errFlag = False
    except KeyError as e:
        pass

    try:
        eel.printAgentDom(data['title'])
        errFlag = False
    except Exception as e:
        pass

    if errFlag:
        eel.printAgentDom("Sorry I didn't find the meaning")
        TextToSpeech.say("Sorry I didn't find the meaning")



# find("mother")
