from functools import reduce

#fruits = ['apple', 'peach', 'pear']
#for fruit in fruits:
#    print(fruit)
    

#Challenge 1: Average Height Calculator

#student_heights = input("Input a list of student heights ").split()
#for n in range(0, len(student_heights)):
#  student_heights[n] = int(student_heights[n])
#
#                                                           My way
#def add(a,b): 
#	return a + b 
#the_sum = reduce(add, student_heights) 
#
#print(round(the_sum / (n+1)))
#student_heights = input("Input a list of student heights ").split()
#for n in range(0, len(student_heights)):
#  student_heights[n] = int(student_heights[n])
#
#
#
#total_height=0                                                     FOR loop way
#for height in student_heights:
#    total_height += height
#
#number_of_students = 0
#for student in student_heights:
#    number_of_students += 1
#    
#result = total_height / number_of_students
#
#print(round(result))

#Challenge 2: Highest score calc
#student_scores = input("Input a list of student scores ").split()
#for n in range(0, len(student_scores)):
#  student_scores[n] = int(student_scores[n])
#
#highest_score = 0
#for score in student_scores:
#    if score > highest_score:
#        highest_score = score
#        
#print (f'The highest score in the class is: {highest_score}')

#total = 0
#for number in range(1,101):
#    total += number
#print(total)

#Challenge 3: guas thing
#total = 0
#for number in range (2,101, 2):
#    total += number
#print (total)

# Challenge 4: fizzbuzz
#for number in range(1,101):
#    
#    if number % 3 == 0 and number % 5 == 0:
#        print('FizzBuzz')
#    elif number % 3 == 0:
#        print('Fizz')
#    elif number % 5 == 0:
#        print('buzz')
#    else:
#        print(number)
#

#Final Challenge: Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ''

for char in range(1, nr_letters + 1):
    password += random.choice(letters)
    
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
    
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

password1 ='' .join(random.sample(password, len(password)))
print(password1)