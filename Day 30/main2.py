import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
word_dict = {
    row.letter: row.code for (index, row) in data.iterrows()
}

run_again = True
while run_again:
    user_name = input("Enter your name: ").upper()
    try:
        code_list = [word_dict[letter] for letter in user_name]
        print(code_list)
    except KeyError:
        print("Sorry, only alphabetic letters are allowed.")
    else:
        run_again = False


