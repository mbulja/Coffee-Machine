from turtle import Screen,Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

l_paddle=Paddle(-370,0)
d_paddle=Paddle(370,0)
scoreboard=Scoreboard()
ball=Ball()
screen.update()

screen.listen()#za interakciju sa tipkama






screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

screen.onkey(d_paddle.up,"Up")
screen.onkey(d_paddle.down,"Down")


game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_wall()

    if ball.distance(d_paddle)<60 and ball.xcor()>350 or ball.distance(l_paddle)<60 and ball.xcor()<-350:
        ball.bounce_paddle()

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.d_point()




screen.exitonclick()
