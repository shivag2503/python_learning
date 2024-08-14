print("Welcome to the Secret Auction")
auction_dict = {}

flag = True

while flag:
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid amount: $"))
    auction_dict[name] = bid
    yes_no = input("Is there any other person available for bidding? Type 'yes' or 'no'..").lower()
    print("\n" * 100)
    if yes_no == "no":
        flag = False


max_bid = 0
winner = ""

for item in auction_dict:
    if auction_dict[item] > max_bid:
        max_bid = auction_dict[item]
        winner = item

print(f"Winner of the Secret Auction is: {winner}")




