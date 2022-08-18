from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()

#challenge 1: Etch a Sketch
#def clear():
#    bruh.reset()
#
#def forwards():
#    bruh.forward(10)
#    
#def backwards():
#    bruh.backward(10)
#    
#def right():
#    new_heading = bruh.heading() - 10
#    bruh.setheading(new_heading)
#    
#def left():
#    new_heading = bruh.heading() + 10
#    bruh.setheading(new_heading)
#screen.listen()
#screen.onkey(key='c', fun=clear)
#screen.onkey(key='w', fun=forwards)
#screen.onkey(key='s', fun=backwards)            Challenge 1 stuff
#screen.onkey(key='a', fun=left)
#screen.onkey(key='d', fun=right)
screen.setup(width = 500,height = 400)

user_bet = screen.textinput(title='Make your Bet:', prompt='Which turtle will win the race? Enter a color: ')
print(user_bet)
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple',]
y_positions = [-125,-75,-25,25,75,125]
turtles = []

for turtle_index in range(0,6):
    new_bruh = Turtle(shape ='turtle')
    new_bruh.color(colors[turtle_index])
    new_bruh.penup()
    new_bruh.goto(x=-220, y=y_positions[turtle_index])
    turtles.append(new_bruh)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost. The {winning_color} turtle is the winner.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()