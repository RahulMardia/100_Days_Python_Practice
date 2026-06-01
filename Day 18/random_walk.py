import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

direction = [0,90,180,270]
tim.pensize(15)
tim.speed(0)
def random_walk(moves):
    for _ in range(moves):
       tim.color(random_color())
       tim.setheading(random.choice(direction))
       tim.forward(40)


random_walk(1000)



screen = Screen()
screen.exitonclick()