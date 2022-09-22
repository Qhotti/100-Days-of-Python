# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['key'])
# except FileNotFoundError:                                         #does this if there is a FileNotFoundError
#     file = open('a_file.txt','w')
#     file.write('something')
# except KeyError as error_message:                                #does this if there is a keyerror
#     print(f'the key {error_message} does not exist.')
# else:
#     content = file.read()
#     print(content)
# finally:                                               #does the code no matter what
#     file.close()
#     print('file closed')
#     raise KeyError             # raising your own errors



    
#height = float(input('Height: '))
#weight = int(input('Weight: '))
#
#
#if height > 3:
#    raise ValueError('brother is a titan')                   # why raise an error
#
#bmi = weight / height ** 2
#print(bmi)


#Challenge 1: IndexError Handling

#fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
#def make_pie(index):
#    try:
#        fruit = fruits[index]
#        print(fruit + " pie")
#    except IndexError:
#        print('Fruit pie')
#        print(None)
#        
#make_pie(4)

#Challenge 2: KeyError Handling

#facebook_posts = [
#    {'Likes': 21, 'Comments': 2}, 
#    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#    {'Comments': 4, 'Shares': 2}, 
#    {'Comments': 1, 'Shares': 1}, 
#    {'Likes': 19, 'Comments': 3}
#]
#
#total_likes = 0
#for post in facebook_posts:
#    try:
#        total_likes = total_likes + post['Likes']
#    except KeyError:
#        pass
#
#
#print(total_likes)





import pandas

on = True

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while on:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('sorry, letters only G.')
    else:
        print(output_list)
        on = False
#def generate_phonetic():
#    word = input("Enter a word: ").upper()
#    try:
#        
#        output_list = [phonetic_dict[letter] for letter in word]     #This method also works.
#    except KeyError:
#        print('sorry, letters only G.')
#        generate_phonetic()
#    else:
#        print(output_list)