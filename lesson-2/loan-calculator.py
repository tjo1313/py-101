"""
This program calculates a monthly loan payment based on three user inputs:
total loan amount, Annual Percentage Rate (APR), and loan duration.
"""

# def invalid_number(number_str):
#     try:
#         float(number_str)
#     except ValueError:
#         return True

#     return False

def calculate_payment(loan_amount, monthly_interest_rate, \
loan_duration_months):
    monthly_payment = loan_amount * (monthly_interest_rate/(1 - \
                        (1 + monthly_interest_rate) ** (-loan_duration_months)))
    formatted_payment = "${:,.2f}".format(monthly_payment)
    print(f'\nYour monthly loan payment is {formatted_payment}\n')

print("Welcome! Let's figure out what your monthly loan payment will be!\n")

while True:

    print("What is the total amount you are looking to finance?")
    loan_amount = float(input())

    # while invalid_number(loan_amount):
    #     print("Hmm... something went wrong. Try another amount please.")
    #     loan_amount = input()

    print("\nWhat is the Annual Percentage Rate (APR)? Enter a %: ")
    apr = float(input())
    monthly_interest_rate = (apr / 100) / 12  # converts APR to monthly rate

    print("\nWhat is the duration of the loan in years?")
    loan_duration = float(input())
    loan_duration_months = loan_duration * 12

    calculate_payment(loan_amount, monthly_interest_rate, loan_duration_months)

    print(f"Would you like to perform another calculation?\n")
    print(f"Enter y/n")
    answer = input()
    if answer and answer[0].lower() != 'y': # accounts for uppercase/empty str
        print("\nSee you next time!")
        break
