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