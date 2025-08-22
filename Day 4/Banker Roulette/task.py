import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

pick_one = random.randint(0, len(friends)-1)
print(f"{friends[pick_one]} is going to pay the bill!")


print(f"{random.choice(friends)} is going to pay the bill!")
