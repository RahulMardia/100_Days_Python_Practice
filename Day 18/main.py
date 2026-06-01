from turtle import Turtle,Screen

small_turtle = Turtle()

small_turtle.shape("turtle")
small_turtle.color("black")

# Challenge: Draw a square
# for i in range(4):
#     small_turtle.forward(100)
#     small_turtle.right(90)


# Challenge: Draw a dashed line
# for i in range(15):
#     small_turtle.forward(10)
#     small_turtle.penup()
#     small_turtle.forward(10)
#     small_turtle.pendown()


# Challenge: Draw Triangle
def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        small_turtle.forward(100)
        small_turtle.right(angle)

for shape in range(3,11):
    draw_shape(shape)















screen = Screen()
screen.exitonclick()