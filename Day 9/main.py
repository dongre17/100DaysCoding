# import modules
import art

print(art.logo)

do_you_wanna_bid = True

bid_history = {}

while do_you_wanna_bid:

    name = input("What is your name.. ")

    bid_price = int(input("How much you wanna Bid? $"))

    bid_history[name] = bid_price

    do_you_wanna_bid = input("Any one else wants to Bid? yes or no .. ").lower() == "yes"

highest_bid = 0
personName = ''

for name in bid_history:
    if bid_history[name] > highest_bid:
        personName = name
        highest_bid = bid_history[name] 

print(f"{personName} has made highest ${highest_bid} bid")