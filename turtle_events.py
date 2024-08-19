from turtle import Turtle, Screen
import random

screen = Screen()

screen.listen()

# Task - 1


# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def move_anti_clockwise():
#     tim.left(10)
#
#
# def move_clockwise():
#     tim.right(10)
#
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_anti_clockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="c", fun=clear_screen)

screen.setup(500, 400)
user_input = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

turtles = []
y = -100

for i in range(0, 6):
    tim = Turtle("turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(-238, y)
    y += 50
    turtles.append(tim)

if user_input:
    is_race_on = True

winner = ""

while is_race_on:
    for t in turtles:
        random_number = random.randint(0, 10)
        t.forward(random_number)
        if t.position()[0] > 230:
            winner = t.pencolor()
            is_race_on = False

if winner == user_input:
    print(f"Your {user_input} turtle wins!!")
else:
    print(f"Your {user_input} turtle lost!!")

screen.exitonclick()

