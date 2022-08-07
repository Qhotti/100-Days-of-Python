############DEBUGGING#####################

# # Describe Problem
#def my_function():
#   for i in range(1, 21): #never reached 20. OG: range(1,20)
#     if i == 20:
#       print("You got it")
#my_function()

# # Reproduce the Bug
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 5) #tried to reach out of index. OG: randint(1,6)
#print(dice_imgs[dice_num])

# # Play Computer
#year = int(input("What's your year of birth?"))
#if year >= 1980 and year <= 1994: # needed to be less than or equal to work properly with 1994
#   print("You are a millenial.")
#elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
#age = int(input("How old are you?")) #convert to int
#if age >= 18: #add equal sign
#    print(f"You can drive at age {age}.") #add f to convert to f-string

# #Print is Your Friend
#pages = 0
#word_per_page = 0
#pages += int(input("Number of pages: ")) #add plus before equals or just delete the variables.
#word_per_page += int(input("Number of words per page: "))#add plus before equals
#total_words = pages * word_per_page
#print(total_words)

# #Use a Debugger
#def mutate(a_list):
#  b_list = []
#  for item in a_list:
#    new_item = item * 2
#    b_list.append(new_item) #indention error
#  print(b_list)
#mutate([1,2,3,5,8,13])