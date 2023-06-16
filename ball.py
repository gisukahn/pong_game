from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.xdirection = 1
        self.ydirection = 1
        self.movespeed = 0.1


    def move(self):
        if self.ycor() == 280:
            self.ydirection *= -1
        elif self.ycor() == -280:
            self.ydirection *= -1


        xcordinate = self.xcor()
        ycordinate = self.ycor()
        new_xcor = xcordinate + 10*self.xdirection
        new_ycor = ycordinate + 10*self.ydirection
        self.goto(new_xcor, new_ycor)

    def reset_position(self):
        self.goto(0,0)
        self.xdirection *= -1
