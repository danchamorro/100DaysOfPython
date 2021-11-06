from turtle import Screen, Turtle


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")


# create a function to draw a line with dashes using penup and pendown
def draw_line_with_dashes(length, number_of_dashes):
    for i in range(number_of_dashes):
        timmy_the_turtle.forward(length)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(length)
        timmy_the_turtle.pendown()


draw_line_with_dashes(10, 10)


screen = Screen()
# close the turtle window on click  #
screen.exitonclick()
