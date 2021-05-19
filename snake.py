import snake
from turtle import *

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtle_body = []
        self.create_snake()

    def create_snake(self):
        for p in STARTING_POSITIONS:
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.setposition(p)
            self.turtle_body.append(turtle)

    def move(self):
        for t in range(len(self.turtle_body) - 1, 0, -1):
            new_x = self.turtle_body[t - 1].xcor()
            new_y = self.turtle_body[t - 1].ycor()
            self.turtle_body[t].goto(new_x, new_y)
        self.turtle_body[0].fd(20)

    def up(self):
        if self.turtle_body[0].heading() != DOWN:
            self.turtle_body[0].setheading(UP)

    def down(self):
        if self.turtle_body[0].heading() != UP:
            self.turtle_body[0].setheading(DOWN)

    def left(self):
        if self.turtle_body[0].heading() != RIGHT:
            self.turtle_body[0].setheading(LEFT)

    def right(self):
        if self.turtle_body[0].heading() != LEFT:
            self.turtle_body[0].setheading(RIGHT)
