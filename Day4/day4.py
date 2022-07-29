import random

#random = random.random() * 5
#print(random)
#

#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)

#Challenge 1: Heads or Tails
#hot = random.randint(0,1)
#
#if hot == 0:
#    print('Heads')
#else:
#    print('Tails')

#Challenge 2: Who will pay tonight 
#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)
#
#
#names_string = input("Give me everybody's names, separated by a comma. ")
#names = names_string.split(", ")
#
#number_of_names = len(names)
#
#count = random.randint(0, number_of_names - 1) #or do person == names(random.choice) far less code same result
#
#person = names[count]
#
#print(f"{person} is going to buy the meal today!")

# nested list (list within a list)

#fruits = ['strawberries, kiwi, apple, grapes']
#vegetables = ['carrot, kale, tomato']
#
#dirty_dozen = [fruits, vegetables]

#Challenge 3 = map thing
#row1 = ["⬜️","⬜️","⬜️"]
#row2 = ["⬜️","⬜️","⬜️"]
#row3 = ["⬜️","⬜️","⬜️"]
#map = [row1, row2, row3]
#print(f"{row1}\n{row2}\n{row3}")
#position = input("Where do you want to put the treasure? ")
#
#horizontal = int(position[0])
#vertical = int(position[1])
#
#selected_row = map[vertical -1]
#selected_row[horizontal -1] = 'X'
#
#print(f"{row1}\n{row2}\n{row3}")


#FINAL Challenge: Rock paper scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

person = input('What do you choose? Rock(0), Paper(1), or Scissors(2) ')

if person == '0':
    print(rock)
elif person == '1':
    print(paper)
else:
    print(scissors)
    
choices = [rock, paper, scissors ]

computer = random.randint(0, len(choices) - 1)

print('Computer chose:')

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)
    
if computer == 0 and person == '2':
    print ('You lose')
elif computer == 1 and person == '0':
    print('You lose')
elif computer == 2 and person == '1':
    print('You lose')
elif person == '0' and computer == 2:
    print ('You win')
elif person == '1' and computer == 0:
    print('You win')
elif person == '2' and computer == 1:
    print('You win')
else:
    print('Draw')