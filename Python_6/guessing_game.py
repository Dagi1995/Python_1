from random import randint
print("***************Wellcome To guessing Game***************")
print("****** I'm thinking of a number between 1and 100*******")
EASY_LEVEL = 10
HARD_LEVEL = 5
answer = randint(1,100)
print(answer)

def chack_answer(answer , guess , turns):
    if answer < guess:
        print("Too high")
        return turns - 1
    elif answer > guess :
        print("Too low") 
        turns - 1  
    else:
        print(f"You got it , the answer was {answer} ")   

def set_difficulty():
    level =  input("Choose a difficulty , type 'easy' or 'hard' : ").lower()
    if level == 'easy':
       return EASY_LEVEL
    else:
        return HARD_LEVEL
def game():  
    turns = set_difficulty()
    guess =0 
    while answer != guess:
        print(f"you have {turns} attempes remaining to guess")    
        guess = int(input("guess a number : "))
        turns = chack_answer(answer , guess ,turns)
        if turns == 0 :
            print("You run out of guess , you loss ")
            return
        elif answer != guess:
            print("Guess Again.")
game()