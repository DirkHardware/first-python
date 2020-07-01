import random


def hi_lo_game():
    highest = 10
    answer = random.randint(1, highest)
    guessed = False

    while not guessed:
        print("Please guess number between 1 and {}: ".format(highest))
        guess = int(input())

        if guess == answer:
            print("You got it right the first time!")
            guessed = True
        else:
            if guess < answer:
                print("Please guess higher")
            else:
                print("Please guess lower")
            guess = int(input())
            if guess == answer:
                print("Well done, you guessed it.")
                guessed = True
            else:
                print("Sorry, you have not guessed correctly.")

guessing_game()
