import turtle
from turtle import *
t = Turtle()


t.shape('turtle')

def square(x):
  t.forward(x)
  t.left(90)
  t.forward(x)
  t.left(90)
  t.forward(x)
  t.left(90)
  t.forward(x)
  t.left(90)
square(200)

turtle.done()
