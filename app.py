from typing import Any
from flask import Flask, render_template, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ =="__main__":
    app.run(debug=True)

#from flask import Flask, render_template, url_for
#from tkinter import *
#from tkinter import filedialog
#import pyttsx3
#import PyPDF2
#app = Flask(__name__)
#@app.route('/')
#def index():
#    return render_template('index.html')
#if __name__ =="__main__":
#    app.run(debug=True)
#root = Tk()
#root.geometry('350*350')
#label_page = Label(root,text="Page Number").pack()
#start_page_number = Entry(root)
#start_page_number.pack()
#label = Label(root,text="Which book you want to read?").pack()
#def fileDialog():
#    path = filedialog.askopenfilename()
#   book = open(path,'rb')
#   pdfReader = PyPDF2.PdfFileReader(book)
#   pages = pdfReader.numPages
#    speaker = pyttsx3.init()
#    for num in range(int(start_page_number.get()),pages):
#        page = pdfReader.getPage(num)
#        txt = page.extractText()
#        print(txt)
#        speaker.say(txt)
#        speaker.runAndWait()
#Button(root,text="Choose Book", command=fileDialog).pack()
#root.mainloop()