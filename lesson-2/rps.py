import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock',]
SHORTENED_CHOICES = ['r', 'p', 's', 'l', 'sp']

def prompt(message):
    print(f"==> {message}")

def get_user_choice():
    while True:
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        prompt("You can also enter 'r' for rock if you don't want to type out \
the entire word! (Use 's' for scissors and 'sp' for spock since they both \
start with 's'.")
        choice = input().lower()
        if choice in VALID_CHOICES or SHORTENED_CHOICES:
            if choice in ('r', 'rock'):
                return 'rock'
            elif choice in ('p', 'paper'):
                return 'paper'
            elif choice in ('s', 'scissors'):
                return 'scissors'
            elif choice in ('l', 'lizard'):
                return 'lizard'
            else:
                return 'spock'
        else:
            prompt(f"Sorry, '{choice}' is not a valid choice. Try again.")

def get_computer_choice():
    return random.choice(VALID_CHOICES)

def determine_winner(player, computer):
    prompt(f'You chose {player} and the computer chose {computer}.')

    if ((player == 'rock' and computer == 'scissors') or
          (player == 'scissors' and computer == 'paper') or
          (player == 'paper' and computer == 'rock') or
          (player == 'rock' and computer == 'lizard') or
          (player == 'lizard' and computer == 'spock') or
          (player == 'spock' and computer == 'scissors') or
          (player == 'scissors' and computer == 'lizard') or
          (player == 'lizard' and computer == 'paper') or
          (player == 'paper' and computer == 'spock') or
          (player == 'spock' and computer == 'rock')):
        return 'player'
    elif ((player == 'rock' and computer == 'paper') or
          (player == 'paper' and computer == 'scissors') or
          (player == 'scissors' and computer == 'rock') or
          (player == 'rock' and computer == 'spock') or
          (player == 'spock' and computer == 'paper') or
          (player == 'paper' and computer == 'lizard') or
          (player == 'spock' and computer == 'lizard') or
          (player == 'lizard' and computer == 'scissors') or
          (player == 'lizard' and computer == 'rock') or
          (player == 'scissors' and computer == 'spock')):
        return 'computer'
    else:
        return 'tie'

def display_winner(winner):
    if winner == 'tie':
        prompt("It's a tie!")
    else:
        prompt(f"{winner.capitalize()} wins!")

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        choice = get_user_choice()
        computer_choice = get_computer_choice()

        winner = determine_winner (choice, computer_choice)
        display_winner(winner)

        if winner == 'player':
            player_score += 1
        elif winner == 'computer':
            computer_score += 1
        
        prompt(f"Score - Player: {player_score} Computer: {computer_score}\n")

        if player_score == 3 or computer_score == 3:
            break

    if player_score == 3:
        prompt("Congratulations, you are the champion!")
    else:
        prompt("Computer is the grand champion!")






        

