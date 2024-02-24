# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt("Welcome to THE Calculator!")

# Ask the user for the first number
prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    prompt ("Please input another number!")
    number1 = input()

# Ask the user for the first number
prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    prompt ("Please input another number!")
    number2 = input()

#Print both numbers
prompt(f'Your numbers are {number1} and {number2}.')

prompt("""What operation would you like to perform?\n1) Add 2) Subtract "
"3) Multiply 4) Divide""")
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt("You must choose 1, 2, 3, or 4")
    prompt ("Please input another selection!")
    operation = input()

match operation:
    case '1':    # addition
        output = int(number1) + int(number2)

    case'2':  # subtraction
        output = int(number1) - int(number2)

    case '3':  # multiplication
        output = int(number1) * int(number2)

    case '4':  # division
        output = int(number1) / int(number2)

prompt(f'The result is {output}')