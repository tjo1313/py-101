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

# munsters_description = "The Munsters are creepy and spooky."
# Return a new string that swaps the case of all of the letters:

# answer = munsters_description.swapcase()
# print(answer)

# Question 6
# Determine whether the name Dino appears in the strings below -- check each string separately:

# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# print('Dino' in str1)
# print('Dino' in str2)

# Question 7
# How can we add the family pet, "Dino", to the following list?

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# flintstones.append("Dino")
# print(flintstones)

# Question 8
# In the previous problem, our first answer added 'Dino' to the list like this:

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")

# How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? 
# Replace the call to append with another method invocation.

# flintstones.extend(["Dino", "Hoppy"])
# print(flintstones)

# Question 9
# Return a new version of this sentence that ends just before the word house. 
# Don't worry about spaces or punctuation: remove everything starting from 
# the beginning of house to the end of the sentence.

# advice = "Few things in life are as important as house training your pet dinosaur."
# Expected return value:
# => 'Few things in life are as important as '

# answer = advice[:38]
# print(answer)

# answer = advice.split("house")[0] ==> returns list based on sep then indexes
# print(answer)

# Question 10
# Replace the word "important" with "urgent" in this string:

advice = "Few things in life are as important as house training your pet dinosaur."

answer = advice.replace("important", "urgent")
print(answer)








