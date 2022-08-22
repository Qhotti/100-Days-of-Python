from turtle import Turtle
X = 0
Y = 240
ALIGNMENT = 'center'
FONT = ('Arial', 30 , 'normal')
FONT2 = ('Arial', 20 , 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup() 
        self.color('white')
        self.goto(X, Y)
        self.write(f'SCORE: {self.score}', align=ALIGNMENT, font=FONT)
        
        
    def game_over(self):
        self.hideturtle()
        self.penup() 
        self.color('black')
        self.goto(5,0)
        self.write(f'GAME OVER.', align=ALIGNMENT, font=FONT2)
        
    def score_increase(self):
        self.score += 1
        self.clear()
        self.color('black')
        self.write(f'Score: {self.score}', align='center', font=('Arial', 30))
        
        
        
        