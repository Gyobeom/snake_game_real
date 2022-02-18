from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",22,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def up_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



