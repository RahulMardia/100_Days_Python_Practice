from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
turtle_list = []
turtle_color = ["Red","Blue","Green","Yellow","Orange","Purple"]
screen.setup(width=500,height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ").lower()

y = -100
for turtles in range(0,6):

   new_turtle = Turtle()
   new_turtle.shape("turtle")
   new_turtle.color(turtle_color[turtles])
   new_turtle.penup()
   new_turtle.goto(-230,y)
   y+=40
   turtle_list.append(new_turtle)

if user_bet :
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor().lower()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color.capitalize()} is the winner!")
            else:
                print(f"You've lost! The {winning_color.capitalize()} is the winner!")









screen.exitonclick()








