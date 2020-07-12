import random


def binary_search(start, stop):
    answer = random.randint(start, stop)
    print("Answer={}".format(answer))
    # In the below instance, the parens are operated on first, so (high - low) = 9. Then the division
    # so 9 gets divided by 2 and rounded down to make 4. The addition of 1 makes it 5, which is the middle
    # of 1 and 10
    guesstimate(start, stop, answer)


def guesstimate(low, high, answer):
    guess = low + (high - low) // 2
    if guess < answer:
        print("{} + ({} - {}) // 2".format(low, high, low))
        print(guess)
        print("We gotta guess higher!")
        low = ++answer
        guesstimate(low, high, answer)
    elif guess > answer:
        print("{} + ({} - {}) // 2".format(low, high, low))
        print(guess)
        print("We gotta guess lower!")
        high = --answer
        guesstimate(low, high, answer)
    else:
        print("{} + ({} - {}) // 2".format(low, high, low))
        print(guess)
        print("You guessed it! The answer was {}".format(answer))
        return answer


binary_search(1, 1000)
