from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
  password_input.delete(0,END)
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  for char in range(nr_letters):
    password_list.append(random.choice(letters))

  for char in range(nr_symbols):
    password_list += random.choice(symbols)

  for char in range(nr_numbers):
    password_list += random.choice(numbers)

  random.shuffle(password_list)

  password = ""
  for char in password_list:
    password += char
    
  password_input.insert(0, f'{password}')
  pyperclip.copy(f'{password}')

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    
    if len(website) < 1 and len(email) < 1 and len(password) < 1:
        messagebox.showinfo(title='😡😡😡😡😡😡', message="bro you didn't even enter anything\n          ☢️INJECTING VIRUS☢️")
    
    
    elif len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(title='😡', message='you forgot to enter something dummy')
    else:
        is_ok = messagebox.askokcancel(title=website,message=(f'These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?'))
        if is_ok:
            with open('data.txt', 'a') as data_file:

                data_file.write(f'{website} | {email} | {password} \n')
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()

    
    


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

website_input = Entry(width=35)
website_input.grid(column=1,row=1,columnspan=2,pady=5)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2,pady=5)


password_input = Entry(width=23)
password_input.grid(column=1,row=3,sticky=E)

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2,row=3,padx=10,pady=5)

add_button = Button(text='Add',width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2,pady=20)



















window.mainloop()