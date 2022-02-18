from turtle import Turtle,Screen

tim = Turtle()

def move_forwards():
    tim.forward(20)

def turn_left():
    tim.left(10)

def turn_back():
    tim.left(180)

def turn_right():
    tim.right(10)

def reset_screen():
    #tim.clear() # This only clears the screen but does not reset the turtles starting position.
    tim.reset()

screen = Screen()
print(screen.window_width())
print(screen.window_width())

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=turn_back)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset_screen)


screen.exitonclick()