from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


def open_score_file():
    with open("highscore.txt", mode="r") as file:
        high_score = file.read()
        return int(high_score)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.high_score = open_score_file()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:  {self.points} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.points += 1
        self.clear()
        self.update_score()

    def reset_screen(self):
        if self.points > self.high_score:
            self.high_score = self.points
            h_score = str(self.high_score)
            with open("highscore.txt", mode="w") as file:
                file.write(h_score)

        self.points = 0
        self.update_score()



