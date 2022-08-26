import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('white')
screen.title('Qhotti Snake')
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
    
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #collision with da food
    if snake.head.distance(food) < 15:
        food.new_location()
        snake.extend()
        scoreboard.score_increase()
        
    
    #wall collision
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -302 or snake.head.ycor() >= 300 or snake.head.ycor() <= -302:
        scoreboard.reset()
        snake.reset()
    
    #collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

        
  























screen.exitonclick()