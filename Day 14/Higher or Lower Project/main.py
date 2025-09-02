import random
from art import logo
from art import vs
from game_data import data

def format_data(account):
    """Takes the account data and formats it for better reading."""
    return f"{account['name']}, {account['description']}, from {account['country']}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower count and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# Display art
print(logo)
score = 0
game_should_continue = True

# Generate a random account from the game data
account_a = random.choice(data)

while game_should_continue:

    account_b = random.choice(data)

    # Format the account data into printable format

    print(f"Account A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    # Ask user for a guess

    # Check if user is correct
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower count of each account
    # Use if statement to check if user is correct
    is_correct = check_answer(guess, account_a["follower_count"], account_b["follower_count"])

    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print("\n" * 20)
        print(logo)
        print(f"You're right! Current score is: {score}")
        account_a = account_b
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

# Score keeping

# Make the game repeatable

# Making account at position B become the account at position A

