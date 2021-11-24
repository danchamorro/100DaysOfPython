from turtle import Turtle, Screen
from snake import Snake
import time

# Snake Game

# Create a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turn of animation
screen.tracer(0)

# Create a snake from the snake class
snake = Snake()

# Listener
screen.listen()
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")


# Move the snake squares to the right until hits the right wall
game_on = True
while game_on:
    # Update the screen to show the new position of the snake squares
    screen.update()
    # Update screen every 0.1 seconds
    time.sleep(0.1)
    # Move the snake
    snake.move_snake()


# Exit on click
screen.exitonclick()
