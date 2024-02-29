VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock',]
SHORTENED_CHOICES = ['r', 'p', 's', 'l', 'sp']

def prompt(message):
    print(f"==> {message}")

def display_winner (player, computer):
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
        prompt("You win!")
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
        prompt("Sorry, the computer wins!")
    else:
        prompt("It's a tie!")

def get_user_choice ():
    while True:
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        prompt("You can also enter 'r' for rock if you don't want to type out \
the entire word! (Use 's' for scissors and 'sp' for spock since they both \
start with 's'.")
        choice = input().lower()
        if choice in VALID_CHOICES or SHORTENED_CHOICES:
            if choice == 'r' or choice == 'rock':
                return 'rock'
            elif choice == 'p' or choice == 'paper':
                return 'paper'
            elif choice == 's' or choice == 'scissors':
                return 'scissors'
            elif choice == 'l' or choice == 'lizard':
                return 'lizard'
            else:
                return 'spock'
        else:
            prompt(f"Sorry, '{choice}' is not a valid choice. Try again.")
        

