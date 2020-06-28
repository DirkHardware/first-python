# name = input("Please enter your name: ")
# # Line below converts input to integer, but will crash if string is given
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)

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

guessing_game()
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

# first_function(input("Give me a number"))

# if age >= 18:
#     print("You're old enough to vote")
# else:
#     print("Go back to middleschool, {0}".format(name))

