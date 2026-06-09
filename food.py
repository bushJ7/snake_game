import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("pink")
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(0.5,0.5)
        self.food_refresh()
        
    def food_refresh(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)