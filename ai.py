from googletrans import Translator
from gtts import gTTS
from tkinter import *


window = Tk()
window.geometry('1600x800')
window.config(bg="grey")
set_bg = PhotoImage(file="logo.png")
label_1 = Label(window, image=set_bg)
label_1.place(x=0, y=0)
e1 = Entry(window, bg="white",fg="black",font=("Arial",25,"bold"))
e1.place(x=20,y=20)


def convert_language():
    a1 = e1.get()
    t1 = Translator()
    t2 = click_option.get()
    if t2 == "afrikaans":
        convert = "af"
    elif t2 == "albanian":
        convert = "sq"
    elif t2 == "amharic":
        convert = "am"
    elif t2 == "arabic":
        convert = "ar"
    elif t2 == "Hindi":
        convert = "hi"
    elif t2 == "English":
        convert = "en"
    trans_text = t1.translate(a1, dest=convert)
    trans_text = trans_text.text
    ob1 = gTTS(text=trans_text, slow=False, lang=convert)
    label_2.config(text=trans_text)
choices = [
    "English",
    "Hindi",
    "arabic",
    "amharic",
    "albanian",
    "afrikaans"
]
click_option = StringVar()
click_option.set("Select Language")
list_drop = OptionMenu(window, click_option, *choices)
list_drop.configure(background="green", foreground="white", font=('Arial',15,"bold"))
list_drop.place(x=400,y=20)

label_2 = Label(window, text="Translated text",bg="black", fg="white",font=("Arial",10,"bold"))
label_2.place(x=180,y=120)

Button_1 = Button(window, text="Translate",bg="red",fg="white",font=("Arial",25,"bold"),command=convert_language)
Button_1.place(x=220,y=200)





window.mainloop()