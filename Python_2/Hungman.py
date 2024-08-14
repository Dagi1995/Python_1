import random
import os



from words import word_list
from stage import logo ,Stages
print(logo)
choisen_word = random.choice(word_list)

# print(f'the word is {choisen_word}')
display = []

word_length = len(choisen_word)
for letter in range(word_length):
    display+="_"


end_of_game = False
lives = 6
while not end_of_game:
    guess = input(" Guess a letter :").lower() 
    os.system('cls')

    if guess in display:
        print(f"you have already guessed {guess}")  
    for position in range(word_length):
        letter = choisen_word[position]

        if letter == guess:
            display[position] = letter
    if guess not in choisen_word:
        print(f"you guess {guess} , wrong letter it's not in the word. you lose a live")
        lives-=1
        print(Stages[lives])
        if lives == 0:
            end_of_game = True
            print("you loss")
    print(f"{' '.join(display)}")  
    if '_' not in display:
        end_of_game = True
        print("you win") 
             
