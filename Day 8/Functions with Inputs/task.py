def great(name):
    print("Hello " + name)
    print("How do you do?")
    print("Isn't the weather nice?")

great("Satya")


def great(name):
    print("Hi " + name)

def calculate_love_score(name1, name2):
    true_count = 0
    love_count = 0

    for letter in name1.lower() + name2.lower():
        if letter in "true":
            true_count += 1
        if letter in "love":
            love_count += 1

    print(f"Your True Love score is: {true_count}{love_count}")

calculate_love_score("Satyaranjan Sabat", "Priyanka Senapati")

