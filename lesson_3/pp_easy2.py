# Question 1
# Write two distinct ways of reversing the list without mutating the original list.

# numbers = [1, 2, 3, 4, 5]

# answer = numbers [::-1] ==> slicing
# print(answer)
# answer2 = list(reversed(numbers))
# print(answer2)

# print(list(range(5, 0, -1)))

# Question 2
# Given a number and a list, determine whether the number is in the list.

# numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

# number1 = 8  # False
# number2 = 95 # True

# print(number1 in numbers)
# print(number2 in numbers)

# Question 3
# Programmatically determine whether 42 lies between 10 and 100, inclusive. 
# Do the same for the values 100 and 101,

my_list = []
for num in range(10, 101, 1):
    my_list.append(num)

print(42 in my_list)

print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))

