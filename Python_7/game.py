
import random
from list import people
def get_random():
     return random.choice(people)

def lower_higher_game(): 
     game_should_continue = True      
     person_a = get_random()
     person_b = get_random()
     score = 0
    
     while game_should_continue:
         person_a = person_b
         person_b = get_random()

         while person_a ==person_b:
             person_b = get_random()
         print(f"Compare A: {person_a['name'] } ,{person_a ['brief_description']} ,from {person_a['country']}")
         print(f"Against B: {person_b['name'] } ,{person_b ['brief_description']} ,from {person_b['country']}")
         person_a_follower = person_a['follower_count']
         person_b_follower = person_b['follower_count']
         guess = input("Guess who is more follower , Type 'A' or 'B' :").lower()
         if ( guess == 'a' and  person_a_follower  >  person_b_follower) or (guess == 'b' and  person_a_follower  <  person_b_follower):
             score = score + 1
             print(f"You're right! Current score: {score}.")
         else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

lower_higher_game()