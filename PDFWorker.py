import PyPDF2
import eel

import TextToSpeech


def PDFrotate(origFileName, rotate):
    try:
        if (rotate not in [0, 90, 180, 360]) or len(origFileName) > 1:
            raise Exception
        pdfFileObj = open(origFileName[0], 'rb')
        # creating a pdf File object of original pdf
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pdfWriter = PyPDF2.PdfFileWriter()

        # rotating each page
        for page in range(pdfReader.numPages):
            # creating rotated page object
            pageObj = pdfReader.getPage(page)
            pageObj.rotateClockwise(rotate)
            # adding rotated page object to pdf writer
            pdfWriter.addPage(pageObj)

        # new pdf file object
        eel.printAgentDom("I am working on your file")
        newFile = open("rotated.pdf", 'wb')

        # writing rotated pages to new file
        pdfWriter.write(newFile)

        # closing the original pdf file object
        pdfFileObj.close()

        # closing the new pdf file object
        newFile.close()
        eel.printAgentDom("Your rotated pdf file is ready")
        TextToSpeech.say("Your rotated pdf file is ready")
    except Exception as e:
        print(e)
        eel.printAgentDom("Inappropriate file type or rotation angle")
        TextToSpeech.say("Inappropriate file type or rotation angle")



def PDFmerge(pdfs):
    try:
        if len(pdfs) < 2:
            raise Exception
        for i in pdfs:
            if i.endswith('.pdf'):
               pass
            else:
                raise Exception
        # creating pdf file merger object
        eel.printAgentDom("I am working on your files")
        pdfMerger = PyPDF2.PdfFileMerger()

        # appending pdfs one by one
        for pdf in pdfs:
            pdfMerger.append(PyPDF2.PdfFileReader(pdf), 'rb')
        with open('merged_copy.pdf', 'wb') as new_file:
            pdfMerger.write(new_file)

        eel.printAgentDom("Your merged pdf file is ready")
        TextToSpeech.say("Your merged pdf file is ready")
    except Exception as e:
        print(e)
        eel.printAgentDom("Inappropriate file type")
        TextToSpeech.say("Inappropriate file type")


def PDFsplit(pdf, splits):
    try:
        if len(pdf) > 1:
            raise Exception
        # creating input pdf file object
        pdf = pdf[0]
        pdfFileObj = open(pdf, 'rb')

        # creating pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # starting index of first slice
        start = 0

        # starting index of last slice
        end = splits[0]

        for i in range(len(splits) + 1):
            # creating pdf writer object for (i+1)th split
            pdfWriter = PyPDF2.PdfFileWriter()

            # output pdf file name
            outputpdf = pdf.split('.pdf')[0] + str(i) + '.pdf'

            # adding pages to pdf writer object
            for page in range(start, end):
                pdfWriter.addPage(pdfReader.getPage(page))

            # writing split pdf pages to pdf file
            with open(outputpdf, "wb") as f:
                pdfWriter.write(f)

            # interchanging page split start position for next split
            start = end
            try:
                # setting split end position for next split
                end = splits[i + 1]
            except IndexError:
                # setting split end position for last split
                end = pdfReader.numPages

        eel.printAgentDom("I am working on your files")
        # closing the input pdf file object
        pdfFileObj.close()
        eel.printAgentDom("Your splitted pdf files are ready")
        TextToSpeech.say("Your splitted pdf files are ready")
    except Exception as e:
        print(e)
        eel.printAgentDom("Inappropriate file type or page number out of range")
        TextToSpeech.say("Inappropriate file type or page number out of range")



def add_watermark(wmFile, pageObj):
    # opening watermark pdf file
    wmFileObj = open(wmFile, 'rb')

    # creating pdf reader object of watermark pdf file
    pdfReader = PyPDF2.PdfFileReader(wmFileObj)

    # merging watermark pdf's first page with passed page object.
    pageObj.mergePage(pdfReader.getPage(0))

    # closing the watermark pdf file object
    wmFileObj.close()

    # returning watermarked page object
    return pageObj


def watermark_pdf(wmFileName, ogFileName):
    try:
        # watermark pdf file name
        mywatermark = wmFileName  # 'rotated_example.pdf'
        origFileName = ogFileName  # 'Sample.pdf'
        newFileName = 'watermarked_example.pdf'

        # creating pdf File object of original pdf
        pdfFileObj = open(origFileName, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pdfWriter = PyPDF2.PdfFileWriter()

        # adding watermark to each page
        for page in range(pdfReader.numPages):
            # creating watermarked page object
            wmpageObj = add_watermark(mywatermark, pdfReader.getPage(page))

            # adding watermarked page object to pdf writer
            pdfWriter.addPage(wmpageObj)

        newFile = open(newFileName, 'wb')

        eel.printAgentDom("I am working on your files")
        # writing watermarked pages to new file
        pdfWriter.write(newFile)
        pdfFileObj.close()
        newFile.close()
        eel.printAgentDom("Your watermarked pdf file is ready")
        TextToSpeech.say("Your watermarked pdf file is ready")
    except Exception as e:
        print(e)
        eel.printAgentDom("Inappropriate file type")
        TextToSpeech.say("Inappropriate file type")

# watermark_pdf('rotated_example.pdf', 'Sample.pdf')


def add_encryption(input_pdf, password):
    try:
        if len(input_pdf) > 1:
            raise Exception
        input_pdf = input_pdf[0]
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_reader = PyPDF2.PdfFileReader(input_pdf)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.encrypt(user_pwd=password, owner_pwd=None,
                           use_128bit=True)
        output_pdf = str(input_pdf.split('.pdf')[0] + str('-encrypted') + '.pdf')
        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)

        eel.printAgentDom("Your encrypted pdf file is ready")
        TextToSpeech.say("Your encrypted pdf file is ready")
    except Exception as e:
        print(e)
        eel.printAgentDom("Inappropriate file type")
        TextToSpeech.say("Inappropriate file type")
