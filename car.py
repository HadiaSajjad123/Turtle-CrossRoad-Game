from turtle import Turtle
import random


INITIAL_DISTANCE=5
MOVE_INCREMENT=4
COLOR=["red","yellow","orange","green","blue","purple","grey","magenta","cyan","brown"]
class Car(Turtle):
  def __init__(self):
    self.all_cars=[]
    self.car_speed=INITIAL_DISTANCE

  def create_car(self):
    random_chance=random.randint(1,6)
    if random_chance==1:
      new_car=Turtle()
      new_car.shape("square")
      new_car.color(random.choice(COLOR))
      new_car.shapesize(stretch_len=2,stretch_wid=1)
      new_car.penup()
      random_y=random.randint(-250,250)
      new_car.goto(250,random_y)
      self.all_cars.append(new_car)


  def move_car(self):
    for car in self.all_cars:
      car.backward(self.car_speed)

  def level_up(self):
    self.car_speed+=MOVE_INCREMENT

