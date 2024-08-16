from turtle import Turtle

STARTING_POSITION=(0,-200)
MOVE_DISTANCE=10
FINISH_LINE_Y=200

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.penup()
    self.go_start()
    self.setheading(90)

  def move_forward(self):
    self.forward(MOVE_DISTANCE)

  def go_start(self):
    self.goto(STARTING_POSITION)

  def is_at_finish_line(self):
    return self.ycor() > FINISH_LINE_Y

 