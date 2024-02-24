import json

LANGUAGE = 'en'

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]

# Load messages from JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)  # contains loaded messages as a Python dict

print(messages['welcome'])

while True:

    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        print(messages['invalid_number'])
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        print(messages['invalid_number'])
        number2 = input()

    prompt("What operation would you like to perform?\n")
    prompt("1) Add 2) Subtract 3) Multiply 4) Divide")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("You must choose 1, 2, 3, or 4")
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(f"The result is {output}")

    prompt(f"Would you like to perform another calculation?\n")
    prompt(f"Enter y/n")
    answer = input()
    if answer and answer[0].lower() != 'y': # accounts for uppercase/empty str
        break
