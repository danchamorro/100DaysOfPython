from turtle import Turtle, Screen, color
import random


is_race_on = False
screen = Screen()
# Set the screen size
screen.setup(width=500, height=400, startx=None, starty=None)
# Create a popup window
user_bet = screen.textinput(title="Make your bet",
                            prompt="What color turtle will win? ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create 6 turtles with different colors and different y positions
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    # Set the turtle starting position.
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    # Set the turtle color
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You have won. The {} turtle is the winner!".format(
                    winning_color))
            else:
                print("You have lost. The {} turtle is the winner!".format(
                    winning_color))
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
