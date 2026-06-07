from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score_board import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("--SNAKE GAME--")
screen.tracer(0)
snake = Snake()
score = Score()
food = Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.head.distance(food) < 15:
        food.food_refresh()
        snake.snake_extend()
        score.increase_score()
        
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        snake.snake_reset()
        score.reset()
        
    
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            snake.snake_reset()
            score.reset()

screen.exitonclick()