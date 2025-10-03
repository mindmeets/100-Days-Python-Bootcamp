PLACEHOLDER = "[name]"

class MailHelper:
    def __init__(self):
        with open("./names/invitee.txt", "r") as names_file:
            names = names_file.readlines()

        with open("./letters/starting_letter.txt") as letters_file:
            letter_contents = letters_file.read()
            for name in names:
                stripped_name = name.strip()
                new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
                with open(f"./output/letter_for_{stripped_name}.txt", mode="w") as letter:
                    letter.write(new_letter)
