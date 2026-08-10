# TODO-1: Ask the user for input
import art
print(art.logo)
print("Welcome to the secret auction program.\n")
name=input("What is your name?: ")
price=int(input("What is your bid?: $"))
# bids={}
# TODO-2: Save data into dictionary {name: price}
# bids[name]=price


# TODO-4: Compare bids in dictionary

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    max(bidding_dictionary, key=bidding_dictionary.get)
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")
# TODO-3: Whether if new bids need to be added
print("\n"*100) #Add new screen
# should_continue=("Are there any other bidders?Type 'yes' or 'no'.\n").lower()

continue_bidding=True
while continue_bidding:
    bids = {}
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = ("Are there any other bidders?Type 'yes' or 'no'.\n").lower()

    # if should_continue not in ["yes", "no"]:
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*20)

# TODO-4: Compare bids in dictionary

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner=""
    # max(bidding_dictionary,key=bidding_dictionary.get)
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner=bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")
