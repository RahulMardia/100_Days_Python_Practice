from turtle import Turtle


style = ('Arial', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write(f"Score: {self.score}", font=style, align='center')

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", font=style, align='center')

    def scoreUp(self):  
        self.score += 1 
        self.clear()
        self.updateScoreBoard()
