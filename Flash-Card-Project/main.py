from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"

#--------------------------------------Database Setup-----------------------------------#

try:
    data = pandas.read_csv("Flash Card Project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Flash Card Project/data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
current_card = {}

#------------------------------------------Backend Logic--------------------------------#

def next_card():
    global current_card, flip_timer
    canvas.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_image,image=front_image)
    canvas.itemconfig(lang_label,text="French",fill="black")
    canvas.itemconfig(word_label,text=current_card['French'],fill="black")
    flip_timer = canvas.after(3000,flip_card)

def is_known():
    data_dict.remove(current_card)
    if len(data_dict):
        to_learn = pandas.DataFrame(data_dict)
        to_learn.to_csv("Flash Card Project/data/words_to_learn.csv", index=False)
        next_card()
    else:
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(lang_label, text="🎉 Done!", fill="black")
        canvas.itemconfig(word_label, text="No more words", fill="black")
        canvas.after_cancel(flip_timer)

def flip_card():
    canvas.itemconfig(canvas_image,image=back_image)
    canvas.itemconfig(lang_label,text="English",fill="white")
    canvas.itemconfig(word_label,text=current_card['English'],fill="white")

#-----------------------------------------UI-------------------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)



canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)



front_image = PhotoImage(file="Flash Card Project/images/card_front.png")
back_image = PhotoImage(file="Flash Card Project/images/card_back.png")
canvas_image = canvas.create_image(400,263,image=front_image)

flip_timer = canvas.after(3000,flip_card)
lang_label = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word_label = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))

canvas.grid(column=0,row=0,columnspan=2)



right_img= PhotoImage(file="Flash Card Project/images/right.png")
wrong_img= PhotoImage(file="Flash Card Project/images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0,width=100,height=100,command=is_known)
right_button.grid(row=1,column=1)

wrong_button = Button(image=wrong_img, highlightthickness=0,width=100,height=100,command=next_card)
wrong_button.grid(row=1,column=0)
next_card()

window.mainloop()