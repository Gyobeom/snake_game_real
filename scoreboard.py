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
        with open("score.txt", mode = 'r') as file:
            self.high_score = file.read()

    def update_scoreboard(self):
        self.clear()
        with open("score.txt", mode ='r') as file:
            self.high_score = file.read()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            with open("score.txt", mode='w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def up_score(self):
        self.score += 1
        self.update_scoreboard()




