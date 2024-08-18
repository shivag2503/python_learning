import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

# timmy_the_turtle.shape("turtle")

# TODO:1 Draw square

# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)

# TODO:2 Draw dashed lines -----------

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     # timmy_the_turtle.pencolor("white")
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     # timmy_the_turtle.pencolor("black")
#     timmy_the_turtle.pendown()

# TODO:3 Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

# n = 3
# angle = 360
color_list = ["red", "green", "blue", "orange", "cornflower blue", "brown", "cyan", "yellow", "orchid"]
#
# for i in range(8):
#     shape_angle = angle / n
#     timmy_the_turtle.pencolor(random.choice(color_list))
#     for j in range(n):
#         timmy_the_turtle.right(shape_angle)
#         timmy_the_turtle.forward(100)
#     n += 1

# TODO:4 Draw a random walk

# directions = [0, 90, 180, 270]
# timmy_the_turtle.speed("fastest")
# timmy_the_turtle.pensize(8)
# turtle.colormode(255)
#
# for i in range(200):
#     color_pallet = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#     timmy_the_turtle.setheading(random.choice(directions))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.color(color_pallet)

#  TODO: 5 Draw Spirograph
current_position = timmy_the_turtle.heading()
timmy_the_turtle.speed("fast")
turtle.colormode(255)
for i in range(1, 37):
    color_pallet = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    timmy_the_turtle.color(color_pallet)
    timmy_the_turtle.setheading(current_position)
    timmy_the_turtle.circle(100)
    current_position += 10


screen = Screen()

screen.exitonclick()
