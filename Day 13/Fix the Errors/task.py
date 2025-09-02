input_num = input("How old are you?")
if type(input_num) != int:
    print("Enter a number next time.")
    try:
        age = int(input_num)
    except ValueError:
        print("Try again..")
        age = int(input("How old are you?"))
else:
    try:
        age = int(input_num)
    except ValueError:
        print("You have typed an invalid number.")
        age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
