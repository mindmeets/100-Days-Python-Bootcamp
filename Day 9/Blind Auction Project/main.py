from art import logo
print(logo)

bids = {}
new_bid = 'yes'
while new_bid != 'no':
    # TODO-1: Ask the user for input
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = bid
    # TODO-3: Whether if new bids need to be added
    new_bid = input("Are there any other bidders? Say 'yes' or 'no': ").lower()
    print("\n" * 30)
    print(logo)

# TODO-4: Compare bids in dictionary
highest_bid = 0
highest_bidder_name = ""
for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]
        highest_bidder_name = key


print(f"{highest_bidder_name} won the bid at ${highest_bid}")

