#with open('Day25\weather-data.csv') as data_file:
#    data = data_file.readlines()
#    print(data)
import csv
from optparse import TitledHelpFormatter
import pandas
# with open('Day25\weather-data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:                                      # hard way of getting one row of data in csv
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)



#data = pandas.read_csv('Day25\weather-data.csv')
#print(data['temp'])                                # good way of getting one row of data in csv using pandas

#data = pandas.read_csv('Day25\weather-data.csv')
#data_dict = data.to_dict()                              #convert to dictionary
#print(data_dict)

#temp_list = data['temp'].to_list()

#average = round(data['temp'].mean() , 2)           #how to get mean of data
#print(average)

#data in column
#print(data.temp.max())

# data in row
#print(data[data.day == 'Monday'])
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == 'Monday']
#temp_in_f = int(monday.temp) * 1.8 + 32            monday temp in farenheit
#print(temp_in_f)

#create a dataframe from scratch

#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
#}
#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")

#squirrel thing
#data = pandas.read_csv('Day25\Central-Park-Squirrel-Census-Squirrel-Data.csv')
#grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
#red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
#black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
#print(grey_squirrels_count)
#print(red_squirrels_count)
#print(black_squirrels_count)
#
#data_dict = {
#    'Fur Color': ["Gray", 'Red', 'Black'],
#    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
#}
#df = pandas.DataFrame(data_dict)
#df.to_csv("squirrel_data.csv")



#U.S. Game

import turtle 

screen = turtle.Screen()
screen.title('U.S. Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
game_is_on = True
states_csv = pandas.read_csv('50_states.csv')
score = 0
state_dict = states_csv.to_dict()


while game_is_on:
    answer = screen.textinput(title=f'Score: {score}/50 ', prompt='Enter State Name.\nend to exit.')

    def new_state():
        turtle.hideturtle()
        turtle.penup() 
        turtle.color('black')
        turtle.goto(x,y)
        turtle.write(state)


    if answer in state_dict['state'].values():
        score += 1
        state = answer
        number = state_dict['state']
        things = state_dict['state'][answer]
        #x = state_dict['x'].get[]
        #y =
        #new_state()
    
    if answer == 'end':
        exit()
    print(things)













turtle.exitonclick()

