from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, score=0, color="white", width=1, speed=0):
        super().__init__(visible=False)
        self.score = score
        self.color(color)
        self.width(width)
        self.speed(speed)
        self.penup()
        self.goto(0, -200)
        self.write("Score: {}".format(self.score),
                   align="center", font=("Arial", 20, "bold"))
        self.hideturtle()

    def update_score(self, score):
        self.clear()
        self.write("Score: {}".format(score), align="center",
                   font=("Arial", 20, "bold"))
