from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Set the screen size
screen.setup(width=500, height=400, startx=None, starty=None)
# Create a popup window
user_bet = screen.textinput(title="Make your bet",
                            prompt="What color turtle will win? ")
print(user_bet)


screen.exitonclick()
