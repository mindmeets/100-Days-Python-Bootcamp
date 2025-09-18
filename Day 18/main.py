# import random
# import turtle as t
# import heroes
#
# timmy = t.Turtle()
# timmy.shape("turtle")
#
# # for _ in range(0, 4):
# #     timmy.left(90)
# #     timmy.forward(100)
#
# # for _ in range(16):
# #     timmy.forward(10)
# #     timmy.penup()
# #     timmy.forward(10)
# #     timmy.pendown()
#
# colours = ["red", "blue", "green", "IndianRed", "orange", "purple", "pink", "brown", "cyan", "wheat"]
# directions = [0, 90, 180, 270]
#
# # def draw_shape(num_sides):
# #     for _ in range(num_sides):
# #         angle = 360 / num_sides
# #         timmy.forward(100)
# #         timmy.right(angle)
# #
# # for shape_side_n in range(3, 11):
# #     timmy.color(random.choice(colours))
# #     draw_shape(shape_side_n)
#
# timmy.speed("fastest")
# # timmy.pensize(15)
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
# # for _ in range(200):
# #     # timmy.color(random.choice(colours))
# #     timmy.color(random_color())
# #     timmy.forward(30)
# #     timmy.setheading(random.choice(directions))
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         timmy.color(random_color())
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)
#
# draw_spirograph(5)
#
# screen = t.Screen()
# screen.exitonclick()
#
# # print(heroes.gen())


import colorgram
import turtle as t
import random

# colors = colorgram.extract('img.jpg', 30)

rgb_colors = [(8, 184, 151), (161, 56, 107), (10, 30, 72), (74, 28, 23), (128, 208, 234), (13, 48, 132), (167, 193, 164), (101, 116, 184), (252, 156, 151), (167, 24, 19), (3, 88, 57)]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

print(rgb_colors)
t.colormode(255)
tim = t.Turtle()

tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()