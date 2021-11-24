from turtle import Turtle, Screen

# Snake Game

# Create a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turn of animation
screen.tracer(0)

# Create snakes starting positions
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# Create three snake squares and color is white
snake_squares = []
for position in starting_positions:
    new_square = Turtle()
    new_square.shape("square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(position)
    snake_squares.append(new_square)

# Move the snake squares to the right until hits the right wall
game_on = True
while game_on:
    # Update the screen to show the new position of the snake squares
    screen.update()
    # Make the tail of the snake follow the head
    for index in range(len(snake_squares) - 1, 0, -1):
        x = snake_squares[index - 1].xcor()
        y = snake_squares[index - 1].ycor()
        snake_squares[index].goto(x, y)
    snake_squares[0].forward(20)
    # Check if the snake hits the right wall
    if snake_squares[0].xcor() > 290:
        game_on = False
        print("Game Over")
        break


# Exit on click
screen.exitonclick()
