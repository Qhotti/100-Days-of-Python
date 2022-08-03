#programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",}

#retrieving item from dictionary
#programming_dictionary["Bug"]

#adding a new item to the dictionary
#programing_dictionary["Loop"] = 'the action of doing something over and over again.'


#empty dictionary
#empty_dictionary = {}

#wipe a dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#loop through a dictionary

#for key in programming_dictionary:
#    print(key)
#    print(programming_dictionary[key])



#Challenge 1: Student Grades
#student_scores = {
#  "Harry": 81,
#  "Ron": 78,
#  "Hermione": 99, 
#  "Draco": 74,
#  "Neville": 62,
#}
#
#student_grades = {}
#
#
#for kid in student_scores:
#    score=student_scores[kid]
#    if score >= 91:
#        student_grades[kid] = 'Outstanding'
#    elif score >= 81:
#        student_grades[kid] = 'Exceeds Expectations'
#    elif score >= 71:
#        student_grades[kid] = 'Acceptable'
#    elif score <= 70:
#        student_grades[kid] = 'Fail'
#
#    
#
#
#print(student_grades)







#Nesting

#capitals = {
#    'France': 'Paris',
#    'Germany': 'Berlin',
#}


#nesting a list in a dictionary

#travel_log = {
#    'France': ['Paris', 'Lille', 'Dijon'],
#}

#Nesting a dictionary in a dictionary

#travel_log = {
#    'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visited': 12},
#    'Germany': {'cities_visited':['Berlin', 'Hamburg', 'Stuttgart',], 'total_visited': 5},
#}

#Nesting Dictionary in a list

#travel_log = [
#    {
#     'country': 'France', #dictionary
#     'cities_visited': ['Paris', 'Lille', 'Dijon'], #dictionary,list
#     'total_visited': 12
#    },
#    {
#     'country': 'Germany', 
#     'cities_visited':['Berlin', 'Hamburg', 'Stuttgart',], 
#     'total_visited': 5
#    },
#]

#Challenge 2: Dictionary in list


#travel_log = [
#{
#  "country": "France",
#  "visits": 12,
#  "cities": ["Paris", "Lille", "Dijon"]
#},
#{
#  "country": "Germany",
#  "visits": 5,
#  "cities": ["Berlin", "Hamburg", "Stuttgart"]
#},
#]
##🚨 Do NOT change the code above
#

#
#def add_new_country(country_visited, times_visited, cities_visited):
#    new_country = {}
#    new_country['country'] = country_visited
#    new_country['visits'] = times_visited
#    new_country['cities'] = cities_visited
#    travel_log.append(new_country)
#    

#
#add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#print(travel_log)



#final challenge

from ast import operator
from art import logo
import os

print(logo)





name = []
bid = []

def script(names, bidss):
    global name
    global bid
    
    names = input("What is your name? ")
    name.append(names)
    bidss = input("What is your bid? ")
    bid.append(bidss)
    
def name_clearer():
    global name
    global bid
    name.clear()
    bid.clear()


script(names = name, bidss = bid)


total = {}
    

def bids(person_name, person_bid):
    total.update({person_name: person_bid})

bids(person_name=str(name[0]), person_bid=str(bid[0]))

name_clearer()



another_person = input("Is there anyone else who wants to bid? Yes or No.\n")

while another_person == 'Yes' or another_person == 'yes':
    if another_person == 'Yes' or another_person == 'yes':
        os.system('CLS')
        print(logo)
        script(names = name, bidss = bid)
        bids(person_name=str(name[0]), person_bid=str(bid[0]))
        name_clearer()
        another_person = input("Is there anyone else who wants to bid? Yes or No.\n")

else:
    winner = max(total, key=total.get)

    print(f'The winner is of the auction is {winner}!')
    




