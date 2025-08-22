import random

random_integer = random.randint(1, 10)
print(random_integer)

random_num_0_to_1 = random.random() * 10
print(round(random_num_0_to_1, 2))

random_float = random.uniform(1, 10)
print(random_float)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")