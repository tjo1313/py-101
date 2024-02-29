'''This game is a variation on rock, paper, scissors that adds two more options
Lizard and Spock (based on Big Bang Theory episode). '''

import random
import display as d

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

print("-----------------------------------------------------------")
print("    WELCOME TO ROCK, PAPER, SCISSORS--EXTREME EDITION!")
print("-----------------------------------------------------------")

while True:

    choice = d.get_user_choice()

    computer_choice = random.choice(VALID_CHOICES)
    
    print(choice)
    print(computer_choice)
    
    d.display_winner (choice, computer_choice)

    d.prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        d.prompt('Please enter "y" or "n"')
        answer = input().lower()

    if answer[0] == 'n':
        d.prompt("Thanks for playing!")
        break