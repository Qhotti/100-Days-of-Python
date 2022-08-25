from turtle import Turtle
import random

FONT = ("Courier", 24, "normal")
FONT2 = ("arial", 30, "normal")
X = -240
Y = 240


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup() 
        self.color('black')
        self.goto(X, Y)
        self.write(f'SCORE: {self.score}',  align = 'left', font=FONT)
        
    def game_over(self):
        self.hideturtle()
        self.penup() 
        self.color('black')
        self.goto(5,0)
        self.write(f'GAME OVER.', align = 'center', font = FONT2)
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.color('black')
        self.goto(X, Y)
        self.write(f'SCORE: {self.score}',  align = 'left', font=FONT)
