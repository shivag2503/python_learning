import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()

screen.onkey(player.move_forward, "Up")

car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move()

    # Next level
    is_level_crossed = player.is_at_finish()
    if is_level_crossed:
        score.update_level()
        player.goto_start()
        car.increase_speed()

    # Collide with car
    for my_car in car.all_cars:
        if my_car.distance(player) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
