import random
import os
from art import logo
def deal_card():
    cards = [11 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10 ,10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare (user_score , computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "You win , with Blackjack"
    elif computer_score == 0 :
        return "lose,oppenent has Blackjack"
    elif user_score > 21 :
        return "you went over ,you lose"
    elif computer_score > 21 :
        return "you win"
    elif user_score > computer_score:
        return "you win "
    else:
        return "you loss"
def play_game():
    print(logo)
    user_card = []
    computer_card = []
    is_game_over = False

    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"{user_card} and the score is {user_score}")
        print(f" computer first card is {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("To use other card type 'y' , to pass type 'n' . : ")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True    
    while computer_score != 0 and computer_score < 17 :
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"The user hand : {user_card} ,and score is {user_score}")
    print(f"The user hand : {computer_card} ,and score is {computer_score}")
    print (compare(user_score=user_score,computer_score=computer_score))   
while input("DO YOU WANT TO A GAME OF BLACKJACK ? Type 'y' or 'n' .... : ")== 'y':
    os.system("cls")
    play_game()
