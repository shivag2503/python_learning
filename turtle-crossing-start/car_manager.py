from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.current_move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.backward(self.current_move_distance)

    def generate_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def increase_speed(self):
        self.current_move_distance += MOVE_INCREMENT



