from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

sb = Scoreboard()

my_snake = Snake()
food = Food()


screen.listen()

screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # Detect collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend_segment()
        sb.increase_score()

    # Detect collision with wall
    if (my_snake.head.xcor() > 275 or my_snake.head.xcor() < -275 or my_snake.head.ycor() > 280
            or my_snake.head.ycor() < -280):
        sb.reset()
        my_snake.reset()

    # Detect collision with tail
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            sb.reset()
            my_snake.reset()


screen.exitonclick()
