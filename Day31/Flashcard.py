from textwrap import fill
import pandas as p
import tkinter as tk
import random
import time as t
import csv
BACKGROUND_COLOR = "#B1DDC6"






data = p.read_csv('spanish_to_english.csv')
dict = data.to_dict(orient='records')
number = 0
card={}


try:
    data = p.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = p.read_csv("data/spanish_to_english.csv")
    dict = original_data.to_dict(orient="records")
else:
    dict = data.to_dict(orient="records")

#----------------------------CHANGE WORD----------------------------------------#

def change_word():
    global card,flip_timer
    window.after_cancel(flip_timer)
    
    card = random.choice(dict)
    

    canvas.itemconfig(image,image=CARD_FRONT)
    canvas.itemconfig(language_text, text='Spanish',fill='black')
    canvas.itemconfig(word_text, text=card['Spanish'],fill='black')
    flip_timer = window.after(3000, flip_card)
    
def flip_card():
    canvas.itemconfig(image,image=CARD_BACK)
    canvas.itemconfig(language_text, text='English',fill='white')
    canvas.itemconfig(word_text, text=card['English'],fill='white')
    
def add_to_words_to_learn():
    pass

def remove_from_words_to_learn():
    dict.remove(card)
    data = p.DataFrame(dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_word()
        




#-------------------------------------------UI-----------------------------------------------#
window = tk.Tk()
window.title('Flashcards')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = tk.Canvas(width=800, height=530, highlightthickness=0,bg=BACKGROUND_COLOR)

CARD_FRONT = tk.PhotoImage(file=r'S:\Code_Projects\100 Days of Python\Day31\images\card_front.png')
CARD_BACK = tk.PhotoImage(file=r'S:\Code_Projects\100 Days of Python\Day31\images\card_back.png')
RIGHT_BUTTON = tk.PhotoImage(file=r'S:\Code_Projects\100 Days of Python\Day31\images\q_right.png')
WRONG_BUTTON = tk.PhotoImage(file=r'S:\Code_Projects\100 Days of Python\Day31\images\wrong.png')


image = canvas.create_image(400,265,image=CARD_FRONT)
canvas.grid(columnspan=2)

#--------------------------------------TEXT--------------------------------------------------------#

language_text = canvas.create_text(400,150, text='Spanish',font=('ariel',40,'italic'),fill='black')
word_text = canvas.create_text(400,263, text='word',font=('ariel',60,'bold'),fill='black')



#------------------------------------------BUTTONS----------------------------------------------------#
right_button = tk.Button(image=RIGHT_BUTTON, highlightthickness=0,bg=BACKGROUND_COLOR,command=remove_from_words_to_learn)
right_button.grid(column=1,row=1)


wrong_button = tk.Button(image=WRONG_BUTTON, highlightthickness=0,bg=BACKGROUND_COLOR,command=add_to_words_to_learn)
wrong_button.grid(row=1)



#------------------------------------------stuff------------------------------------------------------------#

change_word()















window.mainloop()