from tkinter import *
from gtts import gTTS
import os
root = Tk() 
Frame1 = Frame(root,bg = "dark turquoise",height = "150")
Frame1.pack(fill = X)
Frame2 = Frame(root,bg = "dark orchid",height = "750")
Frame2.pack(fill=X)
label = Label(Frame1, text = "Text to Speech Coverter",font =( "Arial Bold", 30),bg = "lightpink")
label.place(x = 60, y = 70)
entry = Entry(Frame2, width = 50,bd = 4, font = 16)
entry.place(x = 70, y = 52)
entry.insert(0, "")
def play():

	language = "en"
	tts = gTTS(text = entry.get(),lang = language,slow = False)
	tts.save("ttsconverted.wav")
	os.system("ttsconverted.wav")
btn = Button(Frame2, text = "SUBMIT",width = "12", pady = 10,font = ("Helvetica", 10),command = play, bg='light goldenrod')
btn.place(x = 245,y = 130)
root.title("Tex To Speech")
root.geometry("600x600")
root.mainloop()
