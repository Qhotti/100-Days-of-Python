################### Scope ####################

#enemies = 1
#
#def increase_enemies():
#  enemies = 2
#  print(f"enemies inside function: {enemies}")
#
#increase_enemies()
#print(f"enemies outside function: {enemies}")


#local scope

# def drink_potion():
#     potion_strength = 2  #available only within function
#     print(potion_strength)
# drink_potion()


# #Global scope

# player_health = 10 #available anywhere

# def drink_potion():
#     potion_strength = 2
#     print(player_health)



#modifying global scope

# enemies = 1

# def increase_enemies():
#   #global enemies # dont change global within local most of the time
#   enemies += 1 # instead just do return enemies + 1
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#global constants

# PI = 3.14159 #uppercase means non changing

# def calc():
#     PI

#Final Challenge: Number Guessing Game

import random,os
from art import logo
from number import numbers

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")



computer_number = 0
attempts = 0
guess = 0


def number_gen():
    return computer_number + random.choice(numbers)
computer_number = number_gen()

#print(f'dont forget to remove this {computer_number}')

difficulty = input('Choose your difficulty: Easy or Hard.\n')

if difficulty == 'Easy' or difficulty == 'easy':
  attempts += 10
elif difficulty == 'Hard' or difficulty == 'hard':
  attempts += 5
else:
      print('Not a valid difficulty.')
      exit()
  

os.system('CLS')

def user_guess():
  guess = int(input('Choose your number.\n'))
  return guess


while attempts >= 0:
  guess = user_guess()
  if guess > computer_number:
    print('Too High\nGuess Again.')
    attempts -= 1
    print(f'You have {attempts} attempts remaining.')
  elif guess == computer_number:
    print(f'You Win! The answer was {computer_number}')
    exit()
  else:
    print('Too Low\nGuess Again.')
    attempts -= 1
    print(f'You have {attempts} attempts remaining.')
  if attempts == 0:
    print(f"You've run out of guesses.You lose. The answer was {computer_number}")
    exit()