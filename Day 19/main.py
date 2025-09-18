from turtle import Turtle, Screen

screen = Screen()

# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# # screen.onkey(key="space", fun=move_forward)
# screen.onkey(fun=move_forward, key="w")
# screen.onkey(fun=move_backward, key="s")
# screen.onkey(fun=turn_left, key="a")
# screen.onkey(fun=turn_right, key="d")
# screen.onkey(fun=clear, key="c")

import random

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ?")
print(user_bet)
colors = ["red", "orange", "green", "blue", "violet", "purple"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + turtle_index * 40)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} wins!")
            else:
                print(f"You've lost! {winning_color} wins!")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()





