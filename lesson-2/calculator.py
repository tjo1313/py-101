# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

print("Welcome to THE Calculator!")

# Ask the user for the first number
print("What's the first number?")
number1 = input()

# Ask the user for the first number
print("What's the second number?")
number2 = input()

#Print both numbers
print(f'Your numbers are {number1} and {number2}.')

print("What operation would you like to perform?\n1) Add 2) Subtract "
      "3) Multiply 4) Divide")
operation = input()

if operation == '1':    # addition
    output = int(number1) + int(number2)

elif operation == '2':  # subtraction
    output = int(number1) - int(number2)

elif operation == '3':  # multiplication
    output = int(number1) * int(number2)

elif operation == '4':  # division
    output = int(number1) / int(number2)

print(f'The result is {output}')