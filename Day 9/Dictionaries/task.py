programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow",
}

print(colours["pear"])

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

for key in programming_dictionary:
    print(key + ": " + programming_dictionary[key])

colours["banana"] = "green"
print(colours)

