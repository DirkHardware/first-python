# name = input("Please enter your name: ")
# # Line below converts input to integer, but will crash if string is given
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)

#Simply chained comparison

def comparison_chain():
    age = int(input("How old are you? "))


    # if age >= 16 and age <=65:
    # is the same as
    if 16 <= age <= 65:
        # When comparing conditions using *and*, Python will stop checking as soon as a condition returns false
        # Both will return the following if the condition is met
        print("Have a good day at work")

def comparison_chain2():
    age = int(input("How old are you?"))

    # When using or, unlike and, the flow control will stop as soon as it finds one that is true

    if age < 16 or age > 65:
        print("Enjoy you free time")
    else:
        print("Have fun at work you poor bastard")

def comparison_chain3():
    day = "Friday"
    temperature = 30
    raining = True

    # Note the operator precedence here.
    # Operator precedence is documented at: https://docs.python.org/3/reference/expressions.html#operator-precedence
    # It is in ascending order. Not is highest, followed by and, trailed by or.
    # A more clear way to render this would be:
    # if (day == "Saturday and temperature > 27) or not raining:
    if day == "Saturday" and temperature > 27 or not raining:
        # The else block will execute because the Truthyness of raining trips the not condition
        # before anything else
        print("Go swimming")
    else:
        print("Learn Python")


def guessing_game():
    answer = 5
    print("Please guess number between 1 and 10: ")
    guess = int(input())

    if guess < answer:
        print("Please guess higher.")
        guess = int(input())
        if guess == answer:
            print("Well done you guessed it.")
        else:
            print("Sorry sport, guess you'll never know")
    elif guess > answer:
        print("Please guess lower.")
        guess = int(input())
        if guess == answer:
            print("Well done, you guess it!")
        else:
            print("Sorry sport, guess you'll never know.")
    else:
        print("You got it the first time.")

# guessing_game()

# Dealing with caps


def name_account_match():
    accounts = ["julia", "anderson", "dan", "debbie"]
    user = input("What is your name?: ")

    for i in range(len(accounts)):
        #casefold() lowercases all the characters, kind of like downcase in Ruby
        if user.casefold() in accounts[i]:
            print("Your account login is {}".format(accounts[i]))
            return "Your account login is {}".format(accounts[i])
        else:
            print("Sorry, I don't think you have an account {}.".format(user))
            return "Sorry, I don't think you have an account {}.".format(user)


# name_account_match()

# An experiment in checking input data using a hypothetical polling booth


def sanitize_age(data):
    acceptable = ["ninety", "eighty", "seventy", "sixty", "fifty", "forty", "thirty", "twenty", "nineteen", "eighteen"]
    accidental = [["ninety", "ninty", "niety", "nity", "ninetey", "nintey"],
                  ["eighty", "eigty", "eihty", "eity", "eightey"],
                  ["seventy", "sevnty", "sventy", "svnty", "svty", "seventey"],
                  ["sixty", "sxty", "sity", "sixtey"],
                  ["fifty", "fivty", "ffty", "fiftey"],
                  ["forty", "fourty", "frty", "fortey"],
                  ["thirty", "thity", "thiry", "thirtey"],
                  ["twenty", "tenty", "twnty", "twentey"],
                  ["nineteen", "ninteen", "ninetteen"],
                  ["eighteen""eigteen", "eihteen", "eightteen"]]

    if len(data) > 3:
        for i in range(len(acceptable)):
            if acceptable[i] in data:
                print("You can vote!")
                return "You can vote!"
        for i in range(len(accidental)):
            for j in range(len(accidental[i])):
                test = accidental[i][j]
                if accidental[i][j] in data and j == 0:
                    print("You can vote!")
                    return "You can vote!"
                elif accidental[i][j] in data:
                    print("I'm sorry, I didn't understand. Did you mean {0}?".format(accidental[i][0]))
                    return "Did you mean {0}?".format(accidental[i][0])
        print("Sorry, I couldn't understand you. Please write your age letters (e.g. 'Eighteen') or numbers (e.g. 18)"
              "Be sure to spell properly.")
        sanitize_age(input("How old are you? "))
    elif len(data) < 4:
        dataint = int(data)
        if dataint > 17:
            print("You can vote!")
            return "You can vote!"
        else:
            wait = 18 - dataint
            if wait == 1:
                print("Come back in a year junior.")
                return "Come back in a year junior"
            else:
                print("Check back in {0} years peewee".format(dataint))
                return "Check back in {0} years peewee".format(dataint)
# sanitize_age(data=input("How old are you? ")

# CONTINUE AND BREAK COMMANDS

def shopping():
    shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

    # for item in shopping_list:
    #     if item != "spam":
    #         print("Buy " + item)

    # OR

    # for item in shopping_list:
    #     if item == "spam":
    #         # When continue appears, it causes everything following it in the loop to be ignored
    #         # and the loop to continue from the top, not unlike a GOTO command from basic.
    #         continue
    #     print("Buy " + item)
    #
    # for item in shopping_list:
    #     if item == "spam":
    #         # Similar to continue but will halt the entire for loop. Useful to ending a process when you've
    #         # found what you've need
    #         break
    # print("Buy " + item)

    item_to_find = "spam"
    # None is roughly equivalent to Null
    found_at = None

    # A better example of a use-case for break
    # for index in range(len(shopping_list)):
    #     if shopping_list[index] == item_to_find:
    #         found_at = index
    #         break

    # This can also be written as:
    if item_to_find in shopping_list:
        found_at = shopping_list.index(item_to_find)
        print("{} found at position {}!".format(item_to_find, found_at))
    else:
        print("{} not found".format(item_to_find))
shopping()

