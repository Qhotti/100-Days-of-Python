# import turtle
# timmy = turtle.Turtle()
# timmy.shape('turtle')
# timmy.color("blue")
# timmy.forward(100)
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

#nice table made with prettytable
import prettytable
table = prettytable.PrettyTable()

table.add_column('Pokemon Name', ['Pikachu', 'Squrtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire',])
table.align = 'l'




print(table)