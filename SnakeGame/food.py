from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(random.randint(-290, 290), random.randint(-290, 290))

    def move_food(self):
        self.goto(random.randint(-290, 290), random.randint(-290, 290))
