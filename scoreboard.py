from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score} ", True, align="Center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True,  align="Center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.clear()
        self.penup()
        self.goto(0, 265)
        self.score += 1
        self.write(f"Score: {self.score} ", True, align="Center", font=("Arial", 24, "normal"))
        self.hideturtle()
