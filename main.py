#pip install pyttsx3
#pip install pypdf2

import Pyttsx3
import PyPDF2

book = open('Python_Programming_wikibooks.pdf', 'rb') #first argument is the name of the book
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(7, pages):
    pages = pdfReader.getpage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()