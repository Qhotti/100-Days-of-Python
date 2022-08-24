import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title('Qhotti Pong')
screen.tracer(0)
game_is_on = True


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()





screen.listen()
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down,'Down')
screen.onkey(l_paddle.up,'w')
screen.onkey(l_paddle.down,'s')


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #collision with top or bottom wall = bounce
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    
    #collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    #collision with right wall = reset ball
    if ball.xcor() >= 390:
        ball.reset_position()
        scoreboard.l_point()
        
    #collision with left wall = reset ball
    if ball.xcor() <= -390:
        ball.reset_position()
        scoreboard.r_point()
        
        
        
        


























screen.exitonclick()