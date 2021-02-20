from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os
import eel
import TextToSpeech



@eel.expose
def pdfToText(filename):
    try:
        # Path of the pdf
        if len(filename) > 1:
            raise Exception
        PDF_file = filename[0]
        # Converting PDF to images
        # Store all the pages of the PDF in a variable
        pages = convert_from_path(PDF_file, 500)

        eel.printAgentDom("I am working on your file it may take time depend upon your file size")
        TextToSpeech.say("I am working on your file it may take time depend upon your file size")
        print("I am working on your file")

        # Counter to store images of each page of PDF to image
        image_counter = 1

        # Iterate through all the pages stored above
        for page in pages:
            filename = "page_" + str(image_counter) + ".jpg"
            page.save(filename, 'JPEG')
            image_counter = image_counter + 1

        # Recognizing text from the images using OCR
        # Variable to get count of total number of pages
        filelimit = image_counter - 1

        # Creating a text file to write the output
        outfile = "pdf_to_text.txt"

        # Open the file in append mode so that
        # All contents of all images are added to the same file
        f = open(outfile, "a")

        # Iterate from 1 to total number of pages
        for i in range(1, filelimit + 1):
            filename = "page_" + str(i) + ".jpg"
            text = str((pytesseract.image_to_string(Image.open(filename))))
            text = text.replace('-\n', '')

            f.write(text)

        # Close the file after writing all the text.
        f.close()
        for i in range(1, filelimit + 1):
            os.remove("page_" + str(i) + ".jpg")
        eel.printAgentDom("Your pdf to text file is ready")
        TextToSpeech.say("Your pdf to text file is ready")
    except Exception as e:
        print(e)
        eel.printAgentDom("Inappropriate file type or format please select pdf")
        TextToSpeech.say("Inappropriate file type or format please select pdf")


def imgToText(imageFile):
    print("inside image to text")
    try:
        print(len(imageFile))
        if len(imageFile) > 1:
            raise Exception
        img = Image.open(imageFile[0])
        eel.printAgentDom("I am working on your file")
        print("I am working on your file")
        # describes image format in the output
        print(img)
        # converts the image to result and saves it into result variable
        result = pytesseract.image_to_string(img)
        # write text in a text file and save it to source path
        with open('img2text.txt', mode='w') as file:
            file.write(result)
        eel.printAgentDom("Your image to text file is ready")
        TextToSpeech.say("Your image to text file is ready")
    except Exception as e:
        print(e)
        eel.printAgentDom("Inappropriate file type or format please select image file")
        TextToSpeech.say("Inappropriate file type or format please select image file")
