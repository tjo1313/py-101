# Question 1
# Write two different ways to remove all of the elements from the 
# following list:

# numbers = [1, 2, 3, 4]

# numbers.clear()
# print(numbers)

# while numbers:
#     numbers.pop()

# print(numbers)

# Question 2
# What will the following code output?

# print([1, 2, 3] + [4, 5])    ==> list concatenation

# Question 3
# What will the following code output?

# str1 = "hello there"
# str2 = str1
# str2 = "goodbye!"
# print(str1)    ==> strings are immutable unless we reassign the variable

# Question 4
# What will the following code output?

# my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
# my_list2 = my_list1.copy()
# my_list2[0]['first'] = 42
# print(my_list1)

# Question 5
# The following function unnecessarily uses two return statements to return 
# boolean values. Can you rewrite this function so it only has one return 
# statement and does not explicitly use either True or False?

# def is_color_valid(color):
#     if color == "blue" or color == "green":
#         return True
#     else:
#         return False
    
# def is_color_valid(color):
#     return color == "blue" or color == "green"

# def is_color_valid(color):
#     return color in ["blue", "green"]

