from turtle import *
from random import *
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5,0.5)
        self.speed(10)
        self.refresh()

    def refresh(self):
        self.goto(randint(-280,280),randint(-280,280))






