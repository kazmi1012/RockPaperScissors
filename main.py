import random
from game_logic import determine_winner
from player import get_user_input
from computer import get_computer_choice
EMOJI_MAP = {
    "rock": "✊", "paper": "👋", "scissors": "✌️"
}

def welcome_user():
    print('Welcome to Rock, Paper, Scissors!')
welcome_user()

def get_emoji(choice):
    return EMOJI_MAP.get(choice)

play_again = "yes"

valid_choices = ["rock", "paper", "scissors"]
user_choice = get_user_input(valid_choices)
computer_choice = get_computer_choice(valid_choices)

player_score = 0
computer_score = 0
draw_score= 0



print(f"You chose: {get_emoji(user_choice)}")
print(f"Computer chose: {get_emoji(computer_choice)}")
result = ""

result = determine_winner(user_choice, computer_choice)
print(result)



play_again = input("Do you want to play again? (yes/no):")

while play_again == "yes":

    user_choice = get_user_input(valid_choices)

    print(f"You chose: {get_emoji(user_choice)}")

    computer_choice = get_computer_choice(valid_choices)

    print(f"Computer chose: {get_emoji(computer_choice)}")

    result = determine_winner(user_choice, computer_choice)

    print(result)

    if result == "You win!":
        player_score += 1

    elif result == "You lose!":
        computer_score += 1
    else:
        draw_score += 1
    
    play_again = input("Do you want to play again? (yes/no): ")

print("Thank you for playing") 
print(f"Your score:",player_score)
print(f"Computer score:",computer_score)   
print(f"Draw:", draw_score)

