import os
from art import logo
print(logo)

bid ={}  
direction = True
   
def find_highest_bidder(bidding_record):
     highest_bid = 0
     winner = ""
     for bidder in bidding_record:
          bid_amount = bidding_record[bidder]
          if bid_amount > highest_bid:
               highest_bid = bid_amount
               winner = bidder
     print(f"The winner is {winner} by the bid of {highest_bid}")           

while direction is True:
     name = input("What is your name ? ")
     price = int(input("WHAT IS YOUR BID ?  $"))
     bid[name] = price
     shoude_cont = input("Do you want add other bid ? type 'yes' or 'no' : ").lower()
     if shoude_cont == "no":
         direction = False
         find_highest_bidder(bid)
     elif shoude_cont == "yes":
          os.system('cls')

