from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        Turtle()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def start_again(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False