from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        starting_positions=[(0,0),(-20,0),(-40,0)]
        for position in starting_positions:
            segment=Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            x=self.segments[i-1].xcor()
            y=self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)


    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)


    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)


    def right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)
    def add_segment(self):
        segment=Turtle()
        segment.color("white")
        segment.shape("square")
        segment.penup()
        x=self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        self.segments.append(segment)
        segment.goto(x,y)








