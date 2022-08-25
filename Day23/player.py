from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEADING = 90
B_HEADING = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.go_to_start()
        self.setheading(HEADING)
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)
        
    def up(self):
        self.setheading(HEADING)
        self.forward(MOVE_DISTANCE)
        
    def down(self):
        self.setheading(B_HEADING)
        self.forward(MOVE_DISTANCE)
        
    def end(self):
        self.goto(0,280)
        
    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
        
