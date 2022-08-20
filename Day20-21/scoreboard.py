from turtle import Turtle, Screen
X = 5
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
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        
        
    def game_over(self):
        self.hideturtle()
        self.penup() 
        self.color('white')
        self.goto(5,0)
        self.write(f'GAME OVER.', align=ALIGNMENT, font=FONT2)
        
    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 30))
        
        
        
        