from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()
score=Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

is_game_on = True
while is_game_on:
  time.sleep(0.1)
  screen.update()
  
  car.create_car()
  car.move_car()

  #detect collision with car
  for cars in car.all_cars:
    if cars.distance(player) < 20:
      is_game_on = False
      score.game_over()
  #detect player successful crossing
  if player.is_at_finish_line():
    player.go_start()
    car.level_up()
    score.new_level()

screen.exitonclick()
