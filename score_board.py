from turtle import Turtle 

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_game_v2/data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.goto(0,280)
        self.color("white")
        self.speed("fastest")
        self.up()
        self.display_score()
        
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}",align="center",font=("Arial",12,"normal"))
        
    def increase_score(self):
        self.score += 1
        self.display_score()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game_v2/data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display_score()
        