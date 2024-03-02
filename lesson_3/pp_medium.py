# Question 1
# Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the 
# days before computers had video screens.

# For this practice problem, write a program that outputs The Flintstones Rock! 
# 10 times, with each line indented 1 space to the right of the line above it. 
# The output should start out like this:
# The Flintstones Rock!
#  The Flintstones Rock!
#   The Flintstones Rock!
#    ...

# str = "The Flinstones Rock!"
# for _ in range(10):
#     print(str)
#     str = " " + str

# for padding in range(1, 11):
#     print(" " * padding + "The Flintstones Rock!")

# Question 2
# Alyssa noticed that this code would fail when the input is a negative number, 
# and asked Alan to change the loop. How can he make this work? Note that we're 
# not looking to find the factors for negative numbers, but we want to handle it 
# gracefully instead of going into an infinite loop.

# Bonus: What is the purpose of number % divisor == 0 in that code?

# def factors(number):
#     divisor = number
#     result = []
#     while divisor > 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result
