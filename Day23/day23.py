import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()



#move
screen.listen()
screen.onkey(player.up,'Up')
screen.onkey(player.down,'Down')
screen.onkey(player.end,'e')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    
    #collision with car
    for cars in car.cars:
        if cars.distance(player) <= 20:
            game_is_on = False
            scoreboard.game_over()
            
    #finish line
    if player.is_at_finish_line():
        scoreboard.increase_score()
        player.go_to_start()
        car.level_up()
            
            
screen.exitonclick()