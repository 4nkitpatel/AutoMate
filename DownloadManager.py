from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import eel
import os
import time

import TextToSpeech


class MyHandler(FileSystemEventHandler):
    i = 1
    final_folder_destination = ''

    def on_modified(self, event):
        # new_name = "new_file_" + str(self.i) + ".txt"
        for filename in os.listdir(folder_to_track):
            self.checkFileExtention(filename)
            src = folder_to_track + "/" + filename
            new_destination = self.final_folder_destination + "/" + filename
            os.rename(src, new_destination)

    def checkFileExtention(self, filename):
        if filename.lower().endswith(('.doc', '.txt', '.docx', '.odt', '.rtf', '.tex', '.wks', '.wps', '.wpd')):
            if not (os.path.exists(folder_destination + "/textFiles")):
                path = os.path.join(folder_destination, "textFiles")
                os.mkdir(path)
                self.final_folder_destination = path
            else:
                self.final_folder_destination = folder_destination + "/textFiles"
        elif filename.lower().endswith(
                ('.jpg', 'jpeg', '.gif', '.png', '.psd', '.bmp', '.ico', '.svg', '.tif', 'tiff')):
            if not (os.path.exists(folder_destination + "/imageFiles")):
                path = os.path.join(folder_destination, "imageFiles")
                os.mkdir(path)
                self.final_folder_destination = path
            else:
                self.final_folder_destination = folder_destination + "/imageFiles"
        elif filename.lower().endswith('.pdf'):
            if not (os.path.exists(folder_destination + '/pdfFiles')):
                path = os.path.join(folder_destination, "pdfFiles")
                os.mkdir(path)
                self.final_folder_destination = path
            else:
                self.final_folder_destination = folder_destination + '/pdfFiles'
        elif filename.lower().endswith(
                ('.mp3', '.aif', '.wav', '.aif', '.cda', '.mid', 'midi', '.mpa', '.ogg', '.wma', '.wpl')):
            if not (os.path.exists(folder_destination + "/audioFiles")):
                path = os.path.join(folder_destination, "audioFiles")
                os.mkdir(path)
                self.final_folder_destination = path
            else:
                self.final_folder_destination = folder_destination + "/audioFiles"
        elif filename.lower().endswith(
                ('.arj', '.deb', '.pkg', '.rar', '.rpm', '.zip', '.7z', '.tar.gz', '.z', '.tar.xz')):
            if not (os.path.exists(folder_destination + "/compressedFiles")):
                path = os.path.join(folder_destination, "compressedFiles")
                os.mkdir(path)
                self.final_folder_destination = path
            else:
                self.final_folder_destination = folder_destination + "/compressedFiles"
        elif filename.lower().endswith(('.bin', '.dmg', '.iso', '.toast', '.vcd')):
            if not (os.path.exists(folder_destination + "/DiscAndMediaFiles")):
                path = os.path.join(folder_destination, "DiscAndMediaFiles")
                os.mkdir(path)
                self.final_folder_destination = path
            else:
                self.final_folder_destination = folder_destination + "/DiscAndMediaFiles"
        elif filename.lower().endswith(('.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sql', '.xml', '.sav', '.tar')):
            if not (os.path.exists(folder_destination + "/DataAndDatabaseFiles")):
                path = os.path.join(folder_destination, "DataAndDatabaseFiles")
                os.mkdir(path)
                self.final_folder_destination = path
            else:
                self.final_folder_destination = folder_destination + "/DataAndDatabaseFiles"
        elif filename.lower().endswith(
                ('.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe', '.gadget', '.jar', '.py', '.wsf')):
            if not (os.path.exists(folder_destination + "/ExecutableFiles")):
                path = os.path.join(folder_destination, "ExecutableFiles")
                os.mkdir(path)
                self.final_folder_destination = path
            else:
                self.final_folder_destination = folder_destination + "/ExecutableFiles"
        elif filename.lower().endswith(('.c', '.class', '.cpp', '.cs', '.h', '.java', '.sh', '.swift', '.vb')):
            if not (os.path.exists(folder_destination + "/ProgrammingFiles")):
                path = os.path.join(folder_destination, "ProgrammingFiles")
                os.mkdir(path)
                self.final_folder_destination = path
            else:
                self.final_folder_destination = folder_destination + "/ProgrammingFiles"
        else:
            if not (os.path.exists(folder_destination + "/OtherFiles")):
                path = os.path.join(folder_destination, "OtherFiles")
                os.mkdir(path)
                self.final_folder_destination = path
            else:
                self.final_folder_destination = folder_destination + "/OtherFiles"


# folder_to_track = "/home/sh4d0w/Pictures/myFolder"
# folder_destination = "/home/sh4d0w/Pictures/newFolder"

folder_to_track = ''
folder_destination = ''

def manageFolder(folder2track, folderDestination):
    global folder_to_track
    global folder_destination
    folder_to_track = folder2track
    folder_destination = folderDestination
    event_handler = MyHandler()
    observer = Observer()
    try:
        observer.schedule(event_handler, folder_to_track, recursive=True)
        observer.start()
        TextToSpeech.say("listening to your folder...")
        eel.printAgentDom("listening to your folder...")
    except OSError as e:
        print(e)
        eel.printAgentDom("Given Path Is Incorrect")
        TextToSpeech.say("Given Path Is Incorrect")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# manageFolder("/home/sh4d0w/Pictures/myFolder", "/home/sh4d0w/Pictures/newFolder")
