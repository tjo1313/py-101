# Question 1
# Will the below code raise an error?

# numbers = [1, 2, 3]
# numbers[6] = 5

# Yes-->Out of index/non-consecutive indexing

# Question 2
# How can you determine whether a given string ends with an exclamation mark?
# use 'endswith()' method-->returns boolean value

# Question 3
# Starting with the string:
# famous_words = "seven years ago..."
# Show two different ways to put the expected "Four score and" in front of it.

# new_famous_words = "Four score and " + famous_words 
# f"Four score and {famous_words}"

# Question 4
# Using the following string, create a new string that contains all lowercase 
# letters except for the first character, which should be capitalized.

# munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
# result = munsters_description.capitalize()
# print(result)

# Question 5
# Starting with the string:

munsters_description = "The Munsters are creepy and spooky."
# Return a new string that swaps the case of all of the letters:

answer = munsters_description.swapcase()
print(answer)