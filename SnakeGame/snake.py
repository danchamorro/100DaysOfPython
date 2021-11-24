from turtle import Turtle, Screen
# Create snakes starting positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Distance the snake moves each time
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_squares = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_square = Turtle()
            new_square.shape("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(position)
            self.snake_squares.append(new_square)

    def move_snake(self):
        # Make the tail of the snake follow the head
        for index in range(len(self.snake_squares) - 1, 0, -1):
            x = self.snake_squares[index - 1].xcor()
            y = self.snake_squares[index - 1].ycor()
            self.snake_squares[index].goto(x, y)
        self.snake_squares[0].forward(MOVE_DISTANCE)
