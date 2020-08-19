# creating a function with variable number of arguments

import os


def centre_text(*args, sep=' ', file=None):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, file=file)


# size = os.get_terminal_size()
# print(size)
# If we wanted to centre contingent on terminal size, we would
# run it like this. However this does not work in PyCharm's terminal

def centre_text_relative(*args, file=None):
    text = ""
    for arg in args:
        text += str(arg) + " "
    term_width = os.get_terminal_size()[0]
    left_margin = (term_width - len(text)) // 2
    print(" " * left_margin, text)


# with open('centered', mode='w') as centered_file:
#     centre_text("Star Trekking", "across the universe", file=centered_file)

def returns_x():
    x = 12
    return x

def print_var(y):
    print(y)


print_var(returns_x())


