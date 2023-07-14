from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
sides = 3
angle = 360 / sides


while sides != 8:
    r = random.random()
    g = random.random()
    b = random.random()
    t.color(r, g, b)
    for _ in range(sides):
        t.forward(50)
        t.right(angle)

    sides += 1
    angle = 360 / sides

screen.exitonclick()