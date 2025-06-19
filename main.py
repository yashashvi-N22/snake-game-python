from turtle import Screen, Turtle
import time
#setup screen
screen = Screen()
screen.setup(640,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.update()

position = [(0,0), (-20,0), (-40,0)]

segments= []

for pos in position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)