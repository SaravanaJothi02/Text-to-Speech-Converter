from tkinter import *
from gtts import gTTS
import os
root = Tk() 
root.title("Text To Speech")
root.geometry("600x600")
Frame1 = Frame(root,bg = "dark turquoise",height = "150")
Frame1.pack(fill = X)
Frame2 = Frame(root,bg = "dark orchid",height = "750")
Frame2.pack(fill=X)
labl = Label(Frame1, text = "Text to Speech Coverter",font =( "Arial Bold", 30),bg = "lightpink")
labl.place(x = 60, y = 70)
inputfield = Entry(Frame2, width = 50,bd = 4, font = 16)
inputfield.place(x = 70, y = 52)
inputfield.insert(0, "")
def convert():
	language = "en"
	tts = gTTS(text = inputfield.get(),lang = language,slow = False)
	tts.save("ttsconverted.wav")
	os.system("ttsconverted.wav")
btn = Button(Frame2, text = "SUBMIT",width = "12", pady = 10,font = ("Helvetica", 10),command = convert, bg='light goldenrod')
btn.place(x = 245,y = 130)
root.mainloop()
