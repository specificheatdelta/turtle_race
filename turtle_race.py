from turtle import Turtle, Screen
import random

# tim = Turtle(shape="turtle")
# leo = Turtle(shape="turtle")
# donna = Turtle(shape="turtle")
# mikey = Turtle(shape="turtle")
# splinter = Turtle(shape="turtle")
# april = Turtle(shape="turtle")
# shredder = Turtle(shape="turtle")


screen = Screen()
screen.setup(width=800, height=600)
#turtles = [tim, leo, donna, mikey, splinter, april, shredder]
colors = ["red", "yellow", "green", "blue", "orange", "violet", "indigo"]
turtles = []
user_choice = screen.textinput(title="Turtle Race", prompt="Choose Turtle Color for Race").lower()
print(user_choice)

x = -380
y = -150
for turtle in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    y += 50

is_race_on = True
while is_race_on:
    for t in turtles:
        if t.xcor() > 368:
            is_race_on = False
            winning_color = t.pencolor()
        t.forward(random.randint(0, 10))

if winning_color == user_choice:
    print(f"Your Turtle {winning_color} wins.")
else:
    print(f"You lose. Winning Turtle is {winning_color}")
#
# for n in turtles:
#     if x <= screen.window_height()
#print(turtles)

# print(screen.window_width())
# print(screen.window_height())
screen.exitonclick()