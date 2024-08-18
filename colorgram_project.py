# import colorgram
#
# color_pallet = colorgram.extract("dot_painting.jpg", 30)
# list_of_colors = []
#
# for i in color_pallet:
#     r = i.rgb[0]
#     g = i.rgb[1]
#     b = i.rgb[2]
#     color = (r, g, b)
#     list_of_colors.append(color)
#
# print(list_of_colors)

import turtle as t
import random

color_list = [(241, 237, 228), (236, 238, 244), (245, 237, 242), (235, 243, 239), (185, 162, 132), (129, 92, 70),
              (79, 93, 118), (147, 161, 180), (179, 152, 162), (210, 207, 135), (28, 35, 49), (119, 79, 92),
              (54, 24, 33), (46, 25, 19), (147, 170, 154), (86, 107, 91), (161, 156, 60), (113, 31, 43),
              (168, 107, 98), (27, 37, 33), (51, 58, 92), (212, 179, 189), (110, 123, 155), (117, 37, 27),
              (161, 107, 118), (219, 178, 170), (177, 202, 186), (180, 187, 209), (106, 144, 116), (67, 75, 35)]

tim = t.Turtle()
tim.penup()
t.colormode(255)


def select_color():
    return random.choice(color_list)


tim.hideturtle()
tim.setheading(225)
tim.forward(200)
tim.setheading(0)

for i in range(10):
    for j in range(10):
        tim.dot(20, select_color())
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = t.Screen()

screen.exitonclick()
