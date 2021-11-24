from turtle import Turtle, Screen

# Snake Game

# Create a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


# Create three snake squares and color is white
snake_squares = []
for i in range(3):
    new_square = Turtle()
    new_square.shape("square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(i * -20, 0)
    snake_squares.append(new_square)


# Exit on click
screen.exitonclick()
