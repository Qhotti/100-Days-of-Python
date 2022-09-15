#numbers = [1,2,3]
#new_list = [n+1 for n in numbers]                  # List comprehension
#print(new_list)

#name = input('name? ')
#new_list = [letter for letter in name]           # splits name by letter and commas
#print(new_list)

#thing = [t * 2 for t in range(1,5)]               # doubles number in range
#print(thing)

#names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#short_names = [name for name in names if len(name) < 5]         # checks length of name and if its under 5, put into new list
#print(short_names)
#long_names = [name.upper() for name in names if len(name) > 5]   
# ^^^^checks length of name and if its above 5, make it uppercase and put into a new list
#print(long_names)



#Challenge 1: Squaring Numbers

#numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#squared_numbers =[num * num for num in numbers]
#print(squared_numbers)



#Challenge 2: Even numbers

#numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#result = [num for num in numbers if num % 2 == 0]
#print(result)


#Challenge 3: Data Overlap

#with open("file1.txt", "r") as file1:
#    n1 = file1.readlines()
#    numbers1 = [int(n.strip()) for n in n1 ]    

#with open("file2.txt", "r") as file2:
#    n2 = file2.readlines()
#    numbers2 = [int(n.strip()) for n in n2 ]

#result = [num for num in numbers1 if num in numbers2]

#print(result)

#import random
#names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

#student_score = {new_key:new_value for item in list} # Dictionary comprehension


#student_score = {student:random.randint(1,100) for student in names} #gives student random score and puts in dictionary
#print(student_score)

#passed_students = {student:score for (student,score) in student_score.items() if score >=60}
# ^^^^puts students who scored > 60 in new dictionary
#print(passed_students)



#Challenge 4: Dictionary Comprehension 1

#sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#split_sentence = sentence.split() #could also be done by just doing (sentence.split()) in the loop
#result = {word:len(word) for word in split_sentence} 
#print(result)


#Challenge 5: Dictionary Comprehension 2

#weather_c = {
#    'Monday': 12,
#    'Tuesday': 14,
#    'Wednesday': 15,
#    'Thursday': 14,
#    'Friday': 21,
#    'Saturday': 22,
#    'Sunday': 24,
#}
#
#
#result = {day:temp*9/5+32 for (day,temp) in weather_c.items()}
#print(result)


#student_dict = {
#    'student': ['Angela', 'James', 'Lily'],
#    'score': [56,76,98]
#}

#looping through dictionary
#for (key,value) in student_dict.items():
#    print(key) # or value

#import pandas
#student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

#loop through data frame
#for (key,value) in student_data_frame.items():
#    print(key) or value

#loop through rows of a data frame
#for (index,row) in student_data_frame.iterrows():
#    if row.student == 'Angela':
#        print(row.score)

#Nato alphabet project
import pandas

nato_alphabet_dict = pandas.read_csv('nato_phonetic_alphabet.csv', header=None, index_col=0, squeeze=True).to_dict()
#print(nato_alphabet_dict)

word = input('Enter word: ').upper()

thing = [letter for letter in word]

result = [nato_alphabet_dict[letter] for letter in thing] 

print(result)

