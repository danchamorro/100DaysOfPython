from turtle import Turtle, Screen


screen = Screen()

# Set the screen size
screen.setup(width=500, height=400, startx=None, starty=None)
# Create a popup window
user_bet = screen.textinput(title="Make your bet",
                            prompt="What color turtle will win? ")
print(user_bet)


tim = Turtle(shape="turtle")
# Set the turtle starting position.
tim.penup()
tim.goto(x=-230, y=100)


screen.exitonclick()
