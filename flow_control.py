# name = input("Please enter your name: ")
# # Line below converts input to integer, but will crash if string is given
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)


def sanitize_age(data = input("How old are you? ")):
    acceptable = ["ninety", "eighty", "seventy", "sixty", "fifty", "forty", "thirty", "twenty"]
    for i in range(len(acceptable)):
        if acceptable[i] in data:
            print("You can vote!")
            return "You can vote!"
        elif len(data) < 4:
            dataint = int(data)
            if dataint > 17:
                print("You can vote!")
                return "You can vote!"


sanitize_age()

# first_function(input("Give me a number"))

# if age >= 18:
#     print("You're old enough to vote")
# else:
#     print("Go back to middleschool, {0}".format(name))

