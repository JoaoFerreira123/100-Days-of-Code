from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #Lendo o arquivo que contém a pontuação máxima
        with open('Day 024 - Files, Directories and Paths\Improved SNAKE GAME\data.txt') as data:
            self.highScore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            #escreve a máxima pontuação no arquivo
            with open('Day 024 - Files, Directories and Paths\Improved SNAKE GAME\data.txt', 'w') as data:
                data.write(f'{self.highScore}')
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
