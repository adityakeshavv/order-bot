#this is just a practice
import random

def get_choices():
    player_choice = input("Enter a choice (rock,paper,scissor): ").strip().lower()
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choice = {"Player":player_choice,"Computer":computer_choice}
    return choice

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock" and computer == "scissors":
        return "Rock smashes Scissors! You win!"
    elif player == "rock" and computer == "paper":
        return "Paper catches Rock! You lost!"
    elif player == "paper" and computer == "rock":
        return "Paper catches Rock!, You win!"
    elif player == "paper" and computer == "scissors":
        return "Scissors cuts Paper!, You lost!"
    elif player == "scissors" and computer == "rock":
        return "Rock smashes scissors!, You lost!"
    elif player == "scissors" and computer == "paper":
        return "Scissors cuts Paper!, You win!"
    
result = get_choices()
final = check_win(result["Player"], result["Computer"])
print(final)
    

