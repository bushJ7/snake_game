from turtle import Turtle
t = Turtle()
POSITION = [(0,0),(-20,0),(-40,0)]
class Snake():
    def __init__(self):
        self.segments = []
        self.default_snake()
        self.head = self.segments[0]
    def default_snake(self):
        for position in POSITION:
            self.add_segment(position)
      
        
    def add_segment(self,position):
        t = Turtle("square")
        t.color("pink")
        t.penup()
        t.goto(position)
        self.segments.append(t)
        
    def snake_move(self):
        for i in range(len(self.segments)-1,0,-1):
            prev_x = self.segments[i-1].xcor()
            prev_y = self.segments[i-1].ycor()
            self.segments[i].goto(prev_x,prev_y)
        self.segments[0].forward(20)
        
    def snake_reset(self):
        for seg in self.segments:
            seg.goto(1000,100)
        self.segments.clear()
        self.default_snake()
        self.head = self.segments[0]
        
    def snake_extend(self):
        self.add_segment(self.segments[-1].position())\
            
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    