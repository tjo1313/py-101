# Write a function that takes a short line of text and prints it within a box.

def print_in_box(string):
    top_border = "+-" + len(string) * "-" + "-+"
    padded_line = "| " + len(string) * " " + " |"
    string_line = "| " + string + " |"

    print(top_border)
    print(padded_line)
    print(string_line)
    print(padded_line)
    print(top_border)




print_in_box('To boldly go where no one has gone before.')
print_in_box('')