from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.high_score = 0
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

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset_screen(self):
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        self.update_score()
