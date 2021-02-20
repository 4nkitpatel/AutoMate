import KeywordList
import Meaning
import RecommendCourse
from SelectToSpeech import selectToSpeech
import ServiceConfig
import speech_recognition as sr
import TextToSpeech
from DownloadManager import manageFolder
from GoogleTranslate import translate
from News import getNews
from OCR import pdfToText, imgToText
from threading import Thread
import eel
from PDFWorker import PDFrotate, PDFmerge, PDFsplit, watermark_pdf, add_encryption

eel.init('web')

@eel.expose
def myCommand():
    """listens for commands"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        eel.printUserDom(command + '\n')
    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('.....................')
        command = myCommand()
    return str(command)


@eel.expose
def getFileName(filename, moduleSelection):
    print("moduleSelection : ", moduleSelection)
    if moduleSelection == "ocr":
        process = Thread(target=pdfToText, args=(filename,))
        process.start()
    elif moduleSelection == "rpdf":
        rotatePDF(filename)
    elif moduleSelection == "mpdf":
        list = filename
        mergePDF(list)
    elif moduleSelection == "spdf":
        splitPDF(filename)
    elif moduleSelection == "wpdf":
        watermarkPDF(filename)
    elif moduleSelection == "epdf":
        encryptPDF(filename)
    elif moduleSelection == "img":
        img2txt(filename)


value = 0
list1 = []
stop_thread = False

@eel.expose
def inputValue(val):
    global value
    value = val

@eel.expose
def SingleQueryinputValue(val, flag):
    print(val, " ", flag)
    if str(flag) == "news":
        getNews(str(val))
    elif str(flag) == "cr":
        RecommendCourse.getUdacityCourse(str(val))
    elif str(flag) == "meaning":
        Meaning.find(str(val))

@eel.expose
def inputPathValue(val):
    print(val)
    global list1
    list1.append(val)
    print(list1)
    if len(list1) == 2:  # TODO miner bug in this if downlaod path is containg only letters it will go to translate
        if "/" in list1[0]:
            process = Thread(target=manageFolder, args=(list1[0], list1[1]))
            process.start()
        else:
            process = Thread(target=translate, args=(list1[0], list1[1]))
            process.start()

        list1 = []


@eel.expose
def check(query):
    print(query)
    if query in KeywordList.news_keywords:
        eel.printAgentDom("which type of news you want?")
        TextToSpeech.say("which type of news you want?")
        eel.getSingleQueryInput("news")
    elif query in KeywordList.ocr_keywords:
        eel.printAgentDom("Please select your pdf")
        TextToSpeech.say("Please select your pdf")
        eel.selectPDF("ocr")
        # problem 1 is pdf should present in current directory // bcz of security of linux it dont give us a full path
    elif query in KeywordList.pdf_keywords:
        if query == 'rotate my pdf':
            eel.printAgentDom("Please type rotation angle and select your file")
            TextToSpeech.say("Please type rotation angle and select your file")
            eel.getInput()
            eel.selectPDF("rpdf")
        elif query == 'merge my pdf':
            eel.printAgentDom("Please select your files")
            TextToSpeech.say("Please select your files")
            eel.selectPDF("mpdf")
        elif query == 'split my pdf':
            eel.printAgentDom("From which page number you want to split. type the page number")
            TextToSpeech.say("From which page number you want to split. type the page number")
            eel.getInput()
            eel.printAgentDom("now please select your pdf")
            TextToSpeech.say("now please select your pdf")
            eel.selectPDF("spdf")
        elif query == 'add watermark to my pdf':
            eel.printAgentDom(
                "Please select your pdf files. first select your watermarked file and then select the original file")
            TextToSpeech.say(
                "Please select your pdf files. first select your watermarked file and then select the original file")
            eel.selectPDF("wpdf")
        elif query == 'encrypt my file with password':
            eel.printAgentDom("please type your password")
            TextToSpeech.say("please type your password")
            eel.getInput()
            eel.printAgentDom("now please select your pdf")
            TextToSpeech.say("now please select your pdf")
            eel.selectPDF("epdf")
    elif query in KeywordList.image2text_keywords:
        eel.printAgentDom("please select your image file")
        TextToSpeech.say("please select your image file")
        eel.selectPDF("img")
    elif query in KeywordList.download_keywords:
        eel.printAgentDom("please type a path of your folder which you want to track")
        TextToSpeech.say("please type a path of your folder which you want to track")
        eel.getPathInput()
        eel.printAgentDom("please type a path of your destination folder")
        TextToSpeech.say("please type a path of your destination folder")
        eel.getPathInput()
    elif query in KeywordList.recommend_course_keywords:
        eel.printAgentDom("which type of course you want")
        TextToSpeech.say("which type of course you want")
        eel.getSingleQueryInput("cr")
    elif query in KeywordList.translate_text_keywords:
        TextToSpeech.say("Enter a Text to Translate")
        eel.printAgentDom("Enter a Text to Translate")
        eel.getPathInput()
        TextToSpeech.say("In Which Language You Want to convert")
        eel.printAgentDom("In Which Language You Want to convert")
        eel.getPathInput()
    elif query in KeywordList.select_to_speech:
        global stop_thread
        eel.printAgentDom("Select And Copy Text To Speech")
        TextToSpeech.say("Select And Copy Text To Speech")
        process = Thread(target=selectToSpeech, args=(lambda: stop_thread,))
        process.start()
        eel.printAgentDom("To exit type exit sts")
        TextToSpeech.say("To exit type exit sts")
    elif query in KeywordList.exit_select_to_speech:
        global stop_thread
        stop_thread = True
        eel.printAgentDom("Exiting Select To speech Service")
        TextToSpeech.say("Exiting Select To speech Service")
        stop_thread = False
        # process = Thread(target=selectToSpeech, args=("exit",))
        # process.start()
    elif query in KeywordList.find_meaning:
        eel.printAgentDom("Type a Word")
        TextToSpeech.say("Type a Word")
        eel.getSingleQueryInput("meaning")
    else:
        ServiceConfig.textMessage(query)


def img2txt(filename):
    process1 = Thread(target=imgToText, args=(filename,))
    process1.start()



def rotatePDF(filename):
    print("angle : ", value)
    process1 = Thread(target=PDFrotate, args=(filename, int(value)))
    process1.start()


def encryptPDF(filename):
    process1 = Thread(target=add_encryption, args=(filename, str(value)))
    process1.start()


def watermarkPDF(filenames):
    list1 = filenames
    process1 = Thread(target=watermark_pdf, args=(list1[0], list1[1]))
    process1.start()


def mergePDF(filenames):
    process1 = Thread(target=PDFmerge, args=(
        filenames,))
    process1.start()


def splitPDF(filename):
    list1 = []
    list1.append(int(value))  # split value can be the list of page number you can split it by comma
    print(list1)
    process = Thread(target=PDFsplit, args=(filename,list1))
    process.start()


eel.start('index.html', size=(400, 650), block=False)


@eel.expose
def speechConversation():
    # TODO if speech mode is on then dont allow to write message so disbale that input text field for UX
    TextToSpeech.say("say exit to Exit Voice Mode")
    while True:
        userSay = myCommand()
        if userSay == "exit":
            TextToSpeech.say("Exiting Voice Mode")
            eel.printAgentDom("Exiting Voice Mode")
            break
        else:
            check(userSay)


while True:
    eel.sleep(0.9)
