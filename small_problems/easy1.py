# 1. Write a function that takes one integer argument and returns True when the 
# number's absolute value is odd, False otherwise.

# def is_odd(number):
#     if abs(number) % 2 == 1:
#         return True
#     else:
#         return False

# result = is_odd(24)
# print(result)

# 2. Print all odd numbers from 1 to 99, inclusive, with each number on a 
# separate line.

# for num in range(1, 100):
#     if num % 2 == 1:
#         print(num)

# for num in range(1, 100, 2):
#     print(num)

# 3. Print all even numbers from 1 to 99, inclusive, with each number on a 
# separate line.

# Bonus Question: Can you solve the problem by iterating over just the even 
# numbers?

# for num in range(2, 100, 2):
#     print(num)

# 4. Build a program that asks the user to enter the length and width of a room, 
# in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# length = float(input("Enter the length of the room in meters: "))
# width = float(input("Enter the width of the room in meters: "))

# area_in_meters = length * width
# area_in_feet = area_in_meters * 10.7639

# print(f"The area of the room in square meters is {area_in_meters:.2f} "
#       f"square meters and {area_in_feet:.2f} square feet.")

# 5. Create a simple tip calculator. The program should prompt for a bill amount
#  and a tip rate. The program must compute the tip, then print both the tip and
# the total amount of the bill. You can ignore input validation and assume that
# the user will enter valid numbers.

# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00

# bill = float(input("What is the bill? "))
# tip_percentage = float(input("What is the tip percentage? ")) / 100
# tip_amount = bill * tip_percentage
# total = bill + tip_amount

# print(f"\nThe tip is ${tip_amount:.2f}")
# print(f"The total is ${total:.2f}")

# 6. Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product of all 
# numbers between 1 and the entered integer, inclusive.

# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.

# number = int(input("Please enter an integer greater than 0: "))
# action = input("Enter 's' to compute the sum, or 'p' to compute the product: ")

# if action == 's':
#     sum = 0
#     for x in range(1, number + 1):
#         sum += x
#     print(f"\nThe sum of the integers between 1 and {number} is {sum:,}.")
# else:
#     product = 1
#     for x in range(1, number + 1):
#         product *= x
#     print(f"\nThe product of the integers between 1 and {number} is {product:,}.")


