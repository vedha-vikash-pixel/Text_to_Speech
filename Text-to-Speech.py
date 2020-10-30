from tkinter import *
from gtts import *
from playsound import playsound

root = Tk()
root.geometry('500x300')
root.config(bg = 'gray')
root.title('TEXT TO SPEECH CONVERTOR')

Label(root, text = 'TEXT_TO_SPEECH' , font='arial 20 bold' , bg ='gray').pack()
Label(root, text ='THANK YOU' , font ='arial 15 bold', bg = 'gray').pack(side = BOTTOM)


Label(root, text ='Enter Text To Convert', font ='arial 15 bold', bg ='gray').place(x=20,y=60)

Msg = StringVar()

entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('vedha.mp3')
    playsound('vedha.mp3')

def Exit():
    root.destroy()

Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =4,bg='green').place(x=100, y=170)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=200,y=170)

root.mainloop()
