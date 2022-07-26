from tkinter import *
import requests as r

quote = ''


def get_quote():
    global quote
    request = r.get('https://api.kanye.rest')
    request.raise_for_status()
    data = request.json()
    quote = data['quote']
    print(len(quote))
    if len(quote) > 125:
        canvas.itemconfig(quote_text,text = f'{quote}',font = ("Arial", 20, "bold"))
    else:
        canvas.itemconfig(quote_text,text = f'{quote}')
    #Write your code here.


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=f"{quote}", width=250, font=("Arial", 24, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()