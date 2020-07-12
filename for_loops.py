# parrot = "Norwegian Blue"
#
# for character in parrot:
#     print(character)

def primitive_separators():
    number = "9,223:372:036 054755:807"
    separators = number[1::4]
    print(separators)

    values = "".join(char if char not in separators else " " for char in number).split()
    print([int(val) for val in values])


def better_separators():
    number = input("Please enter a series of numbers using any separators you like: ")
    separators = ''

    for char in number:
        if not char.isnumeric():
            separators = separators + char

    print(separators)
    values = "".join(char if char not in separators else " " for char in number).split()
    print(sum([int(val) for val in values]))

def get_uppers():
    quote = """
    Alright, but apart from the Sanitation, the Medicine, Education, Wine,
    Public Order, Irrigation, Roads, the Fresh-Water System,
    and Public Health, what have the Romans ever done for us?
    """
    caps = ''

    for char in quote:
        if char.isupper():
            caps = caps + char

    print(caps)
#
# get_uppers()

# A better look at ranges


def simple_range():
    for i in range(1, 21):
        print("i is is now {}".format(i))

# We can add steps to our ranges a la JavaScript as such:


def stepped_range():
    for i in range(0, 11, 2):
        print("i is is now {}".format(i))


# stepped_range()

# Ranges can have negative steps. Behold.


def negative_stepped_range():
    # Notice we didn't need to set the start value to be 11 because for loops are always up to BUT NOT INCLDUING
    for i in range(10, 0, -2):
        print("i is now {}".format(i))


# negative_stepped_range()

# Check to see if a value is in a range

def value_in_range():
    # Compare to comparison_chain2() This is less effecient but
    # def comparison_chain2():
    #     age = int(input("How old are you?"))
    #
    #     # When using or, unlike and, the flow control will stop as soon as it finds one that is true
    #
    #     if age < 16 or age > 65:
    #         print("Enjoy you free time")
    #     else:
    #         print("Have fun at work you poor bastard")
    age = int(input("How old are you? "))

    if age in range(16, 66):
        print("Have fun at work you poor bastard")
    else:
        print("Enjoy your free time")

# value_in_range()

def div_by_7():
    for i in range(0, 101):
        if i % 7 == 0:
            print(i)
    # These solutions also work apparently
    # for i in range(0, 101, 7):
    #   print(i)
    # AND
    # for i in range(0, 101)[::7]:
    #   print(i)


def contrived():
    numbers = [1, 45, 32, 12, 60]

    for numbers in numbers
        if numbers % 8 = 0:
            print("The numbers are unacceptable")
            break
        else:

