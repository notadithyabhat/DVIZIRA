import speech_recognition as sr
import datetime
import pyttsx3
import os
from playsound import playsound
from gtts import gTTS
import time
from tkinter import *

window = Tk()
window.title('Text Learning')
window.geometry('200x200')
lbl = Label(window, text = 'Enter the word:')
lbl.grid(column=0,row=0)
word = Entry(window,bd=5)
word.grid(column=0,row=1)
def clicked():
	global speech
	speech = word.get().lower()
	window.destroy()
btn = Button(window, text="ENTER", command=clicked)
btn.grid(column=0,row=2)

window.mainloop()
print(speech)
engine = pyttsx3.init()
engine.setProperty('rate', 60)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

window2 = Tk()
window2.title(speech.capitalize())
photo = PhotoImage(file = rf"C:\Users\Adithya\Documents\Projects\College\SEM 5\OS\Database\{speech}.png") 
def tapped():
	engine.say(speech)
	engine.runAndWait()
Button(window2, image = photo,command = tapped).pack(side = TOP)
lbl2 = Label(window2,text = f'{speech.capitalize()}').pack()
engine.say(speech)
engine.runAndWait() 

  
window2.mainloop()
