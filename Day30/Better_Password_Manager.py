from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from turtle import width
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get().lower()
    email = email_input.get().lower()
    password = password_input.get()
    new_data = {
        website:{
            'email': email,
            'password': password,
        
    }
        }
    
    
    if len(website) < 1 and len(email) < 1 and len(password) < 1:
        messagebox.showinfo(title='😡😡😡😡😡😡', message="bro you didn't even enter anything\n          ☢️INJECTING VIRUS☢️")
    elif len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(title='😡', message='you forgot to enter something dummy')
        
    else:
        try:
            with open('data.json', 'r') as data_file: 
            #reading old data
                data = json.load(data_file) 
        except FileNotFoundError:
            with open('data.json','w') as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
                #updating old data with new data
                data.update(new_data)
                with open('data.json','w') as data_file:
                    json.dump(data,data_file,indent=4)

        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()

    
    

#--------------------------SEARCH--------------------------#
def search():
    try:
        with open('data.json','r') as data_stuff:
            dict_data= json.load(data_stuff)

            email = dict_data[website_input.get().lower()]['email']
            password = dict_data[website_input.get().lower()]['password']
            
    except KeyError:
        messagebox.showinfo(title='bruh', message="No details for website exist")
    except FileNotFoundError:
        messagebox.showinfo(title='bruh', message="No data file found.")
    else:
        messagebox.showinfo(title=website_input.get().lower(), message=f"Email: {email}\nPassword: {password}")
        

















# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=70,pady=70)

canvas = Canvas(width=200, height=200,highlightthickness=0)
my_pass = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=my_pass)
canvas.grid(column=1,row=0)
# ------------------------------WORDS----------------------------------- # 
website_word = Label(text='Website:', font = ('Arial',10,'bold'))
website_word.grid(column=0,row=1)

Email_words = Label(text='Email/Username:', font = ('Arial',10,'bold'))
Email_words.grid(column=0,row=2)

password_word = Label(text='Password:', font = ('Arial',10,'bold'))
password_word.grid(column=0,row=3)

# ----------------------------INPUTS---------------------------------------#

website_input = Entry(width=23)
website_input.grid(column=1,row=1,sticky=E)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2,pady=5)


password_input = Entry(width=23)
password_input.grid(column=1,row=3,sticky=E)

# ---------------------------BUTTONS-----------------------------------------------------#

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2,row=3,padx=10,pady=5)

add_button = Button(text='Add',width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2,pady=20)

search_button = Button(text='Search',command=search)
search_button.grid(column=2,row=1,sticky=W,padx=10)



















window.mainloop()