from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score=0
        self.d_score=0
        self.goto(-100,200)
        self.write(self.l_score,align="center", font=("Courier",80,"normal"))
        self.goto(100, 200)
        self.write(self.d_score, align="center", font=("Courier", 80, "normal"))

    def update_scoreboard(self):
            self.clear()  # Očisti cijeli ekran
            self.goto(-100, 200)
            self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
            self.goto(100, 200)
            self.write(self.d_score, align="center", font=("Courier", 80, "normal"))
    def l_point(self):

        self.l_score+=1
        self.update_scoreboard()


    def d_point(self):

        self.d_score += 1
        self.update_scoreboard()


