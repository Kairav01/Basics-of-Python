# Inspired by Brad Miller's illustration for How to Think like a
# Computer Scientist:
# http://interactivepython.org/runestone/static/thinkcspy/index.html

import turtle

number_of_turtles = 10

screen = turtle.Screen()

def draw_shape(x, y, n = 20, clear = True):
  if clear:
    writer.clear()
  screen.tracer(0)
  for turtle in screen.turtles():
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
  screen.tracer(1)
  for i in range(n):
    screen.tracer(0)
    move_turtles(screen)
    screen.tracer(1)

# Define the missing components
class MyTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')

def create_turtles(screen, n):
    turtles = []
    for i in range(n):
        t = MyTurtle()
        t.setheading(360/n * i)
        turtles.append(t)
    return turtles

def move_turtles(screen):
    for turtle in screen.turtles():
        turtle.forward(10)
        turtle.left(15)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

create_turtles(screen, number_of_turtles)

draw_shape(0,-150, clear = False)

screen.onclick(draw_shape)

screen.listen()
turtle.done()
