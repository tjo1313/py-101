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

for num in range(1, 100, 2):
    print(num)

