# Write a function that takes a string argument and returns a new string that
# contains the value of the original string with all consecutive duplicate 
# characters collapsed into a single character.


def crunch(string):
    
    if string == '':
        return ''
    else:
        new_string = string[0]
        for char in string:
            if char != new_string[-1]:
                new_string += char
    
    return new_string




# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')


# def crunch(text):
#     index = 0
#     crunched_text = ''

#     while index < len(text):
#         if index == len(text) - 1 or text[index] != text[index + 1]:
#             crunched_text += text[index]

#         index += 1

#     return crunched_text