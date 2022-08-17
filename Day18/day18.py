from turtle import Turtle, Screen
import random
import turtle
import colorgram

bruh = Turtle()


#challenge 1: Draw a square

#sides = 0
#
#def square():
#    bruh.right(90)
#    bruh.forward(100)
#    
#while sides < 4:
#    sides += 1
#    square()

# or use a for loop to do it in less code
#for _ in range(4):
#    bruh.right(90)
#    bruh.forward(100)


#challenge 2: Dashed Line

#while True:
#    
#    bruh.forward(10)
#    bruh.up()
#    bruh.forward(10)
#    bruh.down()
    
#challenge 3: Weird shape thing

#def change_color():
#    R = random.random()
#    B = random.random()
#    G = random.random()
#
#    bruh.color(R, G, B)
#
#
#def shape(sides):
#    angle = 360/sides
#    for _ in range(sides):
#        bruh.forward(100)
#        bruh.right(angle)
#
#for shape_side in range(3,11):
#    change_color()
#    shape(shape_side)

#challenge 4: Draw a random walk

#def change_color():
#    R = random.random()
#    B = random.random()
#    G = random.random()
#
#    bruh.color(R, G, B)
#    
#    
#num = [90,180,270]
#bruh.speed(100)
#bruh.pensize(10)
#def walk():
#    while True:
#        change_color()
#        bruh.setheading(random.choice(num))
#        bruh.forward(30)
#        
#walk()
#    
#
    
#challenge 5: Draw a spirograph
#def change_color():
#    R = random.random()
#    B = random.random()
#    G = random.random()
#
#    bruh.color(R, G, B)
#bruh.speed('fastest')
#for _ in range(73):
#    change_color() 
#    current_heading = bruh.heading()  
#    bruh.circle(100)
#    bruh.setheading(current_heading+5)

#Final Project




turtle.colormode(255)
bruh.speed("fastest")
bruh.penup()
bruh.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
bruh.setheading(225)
bruh.forward(300)
bruh.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    bruh.dot(20, random.choice(color_list))
    bruh.forward(50)

    if dot_count % 10 == 0:
        bruh.setheading(90)
        bruh.forward(50)
        bruh.setheading(180)
        bruh.forward(500)
        bruh.setheading(0)
        

screen = Screen()
screen.exitonclick()




    
