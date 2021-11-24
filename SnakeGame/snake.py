from turtle import Turtle, Screen
# Create snakes starting positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Distance the snake moves each time
MOVE_DISTANCE = 20

# Create direction constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_squares = []
        self.create_snake()
        self.head = self.snake_squares[0]

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
        self.head.forward(MOVE_DISTANCE)

    # Move the snake in the direction of the arrow keys pressed by the user
    def go_up(self):
        # If the snake is going down, then it cannot go up
        if self.head.heading() == DOWN:
            return
        self.head.setheading(UP)

    def go_down(self):
        # If the snake is going up, then it cannot go down
        if self.head.heading() == UP:
            return
        self.head.setheading(DOWN)

    def go_left(self):
        # If the snake is going right, then it cannot go left
        if self.head.heading() == RIGHT:
            return
        self.head.setheading(LEFT)

    def go_right(self):
        # If the snake is going left, then it cannot go right
        if self.head.heading() == LEFT:
            return
        self.head.setheading(RIGHT)
