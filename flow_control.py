# name = input("Please enter your name: ")
# # Line below converts input to integer, but will crash if string is given
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)


def sanitize_age(data = input("How old are you? ")):
    acceptable = ["ninety", "eighty", "seventy", "sixty", "fifty", "forty", "thirty", "twenty"]
    is_type = type(data)
    if is_type == "<class 'str'>":
        for i in range(len(acceptable)):
            if acceptable[i] in data:
                print("This is good data")
    else:
        print(type(data))
        print("This is an integer")


sanitize_age()

# first_function(input("Give me a number"))

# if age >= 18:
#     print("You're old enough to vote")
# else:
#     print("Go back to middleschool, {0}".format(name))

