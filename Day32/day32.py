import smtplib
import datetime as dt
import random
import pandas as p
my_email = 'qhotti_motivation_monday@outlook.com'
password = 'Pfrg8oZtp5@Bs*WS'

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs=my_email,
#         msg='Subject:hello\n\nbody of email'
#                         )

# now = dt.datetime.now()

# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1776,month=7,day=4)
# print(date_of_birth)

# now = dt.datetime.now()
# hour = now.hour
# print(hour)
# day_of_week = now.weekday()

# if day_of_week == 0 and hour == 12:
#     with open('quotes.txt') as quotes:
#         quote_selection = quotes.readlines()
#         quote = random.choice(quote_selection)
        
#     with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
#         connection.starttls()
#         connection.login(user=my_email,password=password)
#         connection.sendmail(
#             from_addr=my_email, 
#             to_addrs=my_email,
#             msg=f'Subject:Monday Motivation\n\n{quote}' ) 





##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv DONE

# 2. Check if today matches a birthday in the birthdays.csv
data = p.read_csv('birthdays.csv')
dict = data.to_dict(orient='records')

now = dt.datetime.now()
month = now.month
day = now.day

letter_choices = ['letter_1.txt','letter_2.txt','letter_3.txt']
brother_month = dict[0]['month']
brother_day = dict[0]['day']
name = dict[0]['name']





# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


#if month == brother_month and day == brother_day:
if 1 == 1:
    choice = random.choice(letter_choices)
    with open(choice) as letter:
        letter_contents = letter.read()
        new_letter = letter_contents.replace('[NAME]', name)
        with open(f"letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
            
            
# 4. Send the letter generated in step 3 to that person's email address.
finished_letter = f'letter_for_{name}.txt'
with open(finished_letter) as theletter:
        letter = theletter.readlines()
        print(letter)
# with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
    
#         connection.sendmail(
#             from_addr=my_email, 
#             to_addrs=my_email,
#             msg=f'Subject:Happy Birthday!\n\n{completed_letter}' ) 