from turtle import Turtle
X = 0
Y = 240
FONT = ('Arial', 24 , 'normal')
FONT2 = ('Arial', 20 , 'normal')


    


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('Day24/updated_snake_game/data.txt') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup() 
        self.color('black')
        self.goto(X, Y)
        self.write(f'Score: {self.score} High Score: {self.high_score}' , align='center', font=FONT)
        
    
    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}' , align='center', font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('Day24/updated_snake_game/data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_score()
        
        
        
    def score_increase(self):
        self.score += 1
        self.update_score()
        
        
        
        