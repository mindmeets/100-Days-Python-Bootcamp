import random

rock = '''
---rock---
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
---paper---
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
---scissors---
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gestures = [rock, paper, scissors]
print("'0' for rock.\n'1' for paper.\n'2' for scissors.\nEnter your choice: ")
choice = int(input())

if choice > 2 or choice < 0:
    print("Invalid choice! You lose!")
else:
    computer_choice = random.randint(0, 2)

    print(f"You chose:\n{gestures[choice]}")
    print(f"Computer chose:\n{gestures[computer_choice]}")

    if choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and choice == 2:
        print("You lose!")
    elif computer_choice > choice:
        print("You Lose!")
    elif computer_choice == choice:
        print("It's a tie!")
    else:
        print("You Win!")
