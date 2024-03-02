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

# Question 3

# def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
#     buffer.append(new_element)
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
#     buffer = buffer + [new_element]
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# Question 4
# What will the following two lines of code output?

# print(0.3 + 0.6)
# print(0.3 + 0.6 == 0.9)

# Question 5
# What do you think the following code will output?

# nan_value = float("nan")

# print(nan_value == float("nan")) ==> False

# Question 6
# What is the output of the following code?

# answer = 42

# def mess_with_it(some_number):
#     return some_number + 8

# new_answer = mess_with_it(answer)

# print(answer - 8)    ==> 34 (global variable)

# Question 7
# One day, Spot was playing with the Munster family's home computer, and he wrote
#  a small program to mess with their demographic data:

# munsters = {
#     "Herman": {"age": 32, "gender": "male"},
#     "Lily": {"age": 30, "gender": "female"},
#     "Grandpa": {"age": 402, "gender": "male"},
#     "Eddie": {"age": 10, "gender": "male"},
#     "Marilyn": {"age": 23, "gender": "female"},
# }

# def mess_with_demographics(demo_dict):
#     for key, value in demo_dict.items():
#         value["age"] += 42
#         value["gender"] = "other"

# After writing this function, he typed the following code:
        
# mess_with_demographics(munsters)

# Before Grandpa could stop him, Spot hit the Enter key with his tail. 
# Did the family's data get ransacked? Why or why not? ==> YES

# Question 8
# Function and method calls can take expressions as arguments. Suppose we define 
# a function named rps as follows, which follows the classic rules of the 
# rock-paper-scissors game, but with a slight twist: in the event of a tie, it 
# just returns the choice made by both players.

# def rps(fist1, fist2):
#     if fist1 == "rock":
#         return "paper" if fist2 == "paper" else "rock"
#     elif fist1 == "paper":
#         return "scissors" if fist2 == "scissors" else "paper"
#     else:
        # return "rock" if fist2 == "rock" else "scissors"

# What does the following code output?    ==> "paper"

# print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# Question 9
# Consider these two simple functions:

# def foo(param="no"):
#     return "yes"

# def bar(param="no"):
    # return param == "no" and foo() or "no"

# What will the following function invocation return?

# bar(foo())  ==> "no"

# Question 10
# In Python, every object has a unique identifier that can be accessed using the
# id() function. This function returns the identity of an object, which is g
# uaranteed to be unique for the object's lifetime. For certain basic immutable 
# data types like short strings or integers, Python might reuse the memory 
# address for objects with the same value. This is known as "interning".

# Given the following code, predict the output:

# a = 42
# b = 42
# c = a

# print(id(a) == id(b) == id(c))    ==> TRUE

# print(id(a))
# print(id(b))
# print(id(c))
















































