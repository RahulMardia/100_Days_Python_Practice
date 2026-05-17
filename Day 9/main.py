from art import logo

print(logo)
name = input("What is your name?: ")
price = int(input("What is your bid?: $ "))
bids = {
    name:price
}

def max_bidder(bids):
    highest_bid = 0
    winner = ""
    for bid in bids:
        bid_amount = bids[bid]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")


continue_bidding  = True
while continue_bidding :
    more_bids = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if more_bids == "yes":
        continue_bidding = True
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $ "))
        bids.update({
            name: price
        })
    else:
        continue_bidding = False
        max_bidder(bids)

