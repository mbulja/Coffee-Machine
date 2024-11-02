from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")

score=Scoreboard()
snake=Snake()
food=Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.segments[0].distance(food)<15:
            food.refresh()
            snake.add_segment()
            score.adding_score()
            score.update()
        if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
            game_is_on=False
        for i in range(len(snake.segments)-1,0,-1):
            if snake.segments[0].distance(snake.segments[i])<10:
                game_is_on=False

screen.clear()
screen.bgcolor("black")
score.gameover()




screen.exitonclick()