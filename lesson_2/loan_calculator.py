"""
This program calculates a monthly loan payment based on three user inputs:
total loan amount, Annual Percentage Rate (APR), and loan duration.
"""

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True

    return False

prompt("Welcome! Let's figure out what your monthly loan payment will be!")

while True:

    prompt("----------------------------------------------------------------")
    prompt("What is the loan amount?")
    
    amount = input()
    while invalid_number(amount):
        prompt("Hmm... something went wrong. Please enter a positive number.")
        amount = input()
    
    prompt("What is the interest rate?")
    prompt("(Example: Enter 5 for 5% or 2.5 for 2.5%)")

    interest_rate = input()

    while invalid_number(interest_rate):
        prompt("Hmm... something went wrong. Please enter a positive number.")
        interest_rate = input()

    prompt("What is the loan duration in years?")
    years = input()

    while invalid_number(years):
        prompt("Hmm... something went wrong. Please enter a positive number.")
        years = input()
   
    annual_interest_rate = float(interest_rate) / 100
    monthly_interest_rate = annual_interest_rate / 12
    months = float(years) * 12
    loan_amount = float(amount)
   
    monthly_payment = loan_amount * (
        monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) ** (-months))
    )
    
    prompt(f"Your monthly payment is: ${monthly_payment:.2f}\n")

    prompt("Would you like to perform another calculation?\n")
    prompt("Enter y/n")
    answer = input().lower()
    if answer and answer[0] != 'y': # accounts for empty str
        prompt("See you next time!")
        break
