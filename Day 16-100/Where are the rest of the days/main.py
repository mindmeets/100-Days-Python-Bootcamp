# From Day 16 onwards, you will be creating your own PyCharm projects from scratch.
# Instead of using templates that I have created for you.
# It will be another step in your journey as a developer!
# But don't worry, I will explain how to do everything in the video tutorials on Udemy.

# import random
#
# print("Here is a random number from 1 to 100")
# print(random.randint(1, 100))

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.setup(1600, 900)
# my_screen.bgcolor("black")
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'

print(table)

