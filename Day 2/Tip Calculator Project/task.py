print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

result = (bill / people) * (1 + tip / 100)
print(f"Your total bill is:${round(result, 2)}")


