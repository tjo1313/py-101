'''This game is a variation on rock, paper, scissors that adds two more options
Lizard and Spock (based on Big Bang Theory episode). '''

import random
import display as d

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

while True:

    d.prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice =input().lower()

    while choice not in VALID_CHOICES:
        d.prompt(" That's not a valid choice. Please try again.")
        choice = input().lower()

    computer_choice = random.choice(VALID_CHOICES)

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