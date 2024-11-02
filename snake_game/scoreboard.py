from turtle import Turtle
from snake import Snake
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.update()
        self.hideturtle()
        self.shapesize(1,1)
    def update(self):
        self.clear()
        self.write("Score: " + str(self.score),align="center",font=("Arial",24,"normal"))
    def adding_score(self):
        self.score+=1

    def gameover(self):
        self.goto(0,0)
        self.write("Final score: "+str(self.score),align="center",font=("Arial",24,"normal"))
        self.goto(0,-35)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

