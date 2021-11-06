from turtle import Screen, Turtle
import random


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")


# create a function to draw a line with dashes using penup and pendown
def draw_line_with_dashes(length, number_of_dashes):
    for _ in range(number_of_dashes):
        timmy_the_turtle.forward(length)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(length)
        timmy_the_turtle.pendown()


#draw_line_with_dashes(10, 10)


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]  # list of colours
directions = [0, 90, 180, 270]  # list of directions
timmy_the_turtle.pensize(15)  # set the pen size
timmy_the_turtle.speed("fastest")  # set the speed

for _ in range(200):  # loop 200 times
    # choose a random colour from the list
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.forward(30)  # move forward 30 pixels
    # set the heading to a random direction from the list
    timmy_the_turtle.setheading(random.choice(directions))


screen = Screen()
# close the turtle window on click  #
screen.exitonclick()
