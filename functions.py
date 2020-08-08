# creating a function with variable number of arguments

import os


def centre_text(*args, sep = ' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# size = os.get_terminal_size()
# print(size)
# If we wanted to centre contingent on terminal size, we would
# run it like this. However this does not work in PyCharm's terminal

def centre_text_relative(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    term_width = os.get_terminal_size()[0]
    left_margin = (term_width - len(text)) // 2
    print(" " * left_margin, text)


centre_text("Star Trekking", "across the universe", sep = ',')