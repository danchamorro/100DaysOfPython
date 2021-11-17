from turtle import Turtle, Screen, color


screen = Screen()

# Set the screen size
screen.setup(width=500, height=400, startx=None, starty=None)
# Create a popup window
user_bet = screen.textinput(title="Make your bet",
                            prompt="What color turtle will win? ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]

# Create 6 turtles with different colors and different y positions
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    # Set the turtle starting position.
    tim.penup()
    tim.goto(x=-230, y=y_pos[turtle_index])
    # Set the turtle color
    tim.color(colors[turtle_index])


screen.exitonclick()
