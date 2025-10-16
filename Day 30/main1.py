# #FileNotFound
# # with open("data.txt") as file:
# #     file.read()
#
# #KeyError
# # a_dictionary = {"key": "value"}
# # value = a_dictionary["no_key"]
#
#
# #IndexError
# # fruit_list = ["apple", "banana", "orange"]
# # fruit = fruit_list[3]
#
# #TypeError
# # text = "abc"
# # print(text + 5)
#
# try:
#     file = open("test.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("test.txt", "w")
#     file.write("Something went right")
#     print("File not found")
# except KeyError as error_message:
#     print("KeyError")
#     print(f"{error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("Closing file")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Height must not be over 3 meters.")

bmi = weight / (height * height)
print(bmi)




