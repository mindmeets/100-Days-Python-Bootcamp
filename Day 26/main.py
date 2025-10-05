# name = "Angela"
# new_list = [letter.capitalize() for letter in name]
# print(new_list)
#
# range_list = [item * 2 for item in range(1, 5) if item % 2 == 0]
# print(range_list)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)


# with open("file1.txt") as file1:
#     list1 = [item.strip() for item in file1.readlines()]
#     # print(list1)
#
# with open("file2.txt") as file2:
#     list2 = [item.strip() for item in file2.readlines()]
#     # print(list2)
#
#
# result = [int(item) for item in list1 if item in list2]
#
# print(result)

# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {
#     name: random.randint(30, 99) for name in names
# }
#
# print(students_scores)
#
# first_grade = {
#     key: value for (key, value) in students_scores.items()
#     if value > 59
# }
#
# print(first_grade.keys())

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.student, row.score)

