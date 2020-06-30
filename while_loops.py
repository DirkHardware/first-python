# for i in range(10):
#     print("i is now {}".format(i))

def no_exit():
    available_exits = ["north", "south", "east", "west"]
    chosen_exit = ""

    while chosen_exit not in available_exits:
        chosen_exit = input("Please choose a direction: ")
        if chosen_exit.casefold() == "quit":
            # you can use lower but apparently casefold handles weird shit like german
            print("Gave over")
            break
    print("aren't you glad you got out of there")

# no_exit()

def stop_at_11():
    for i in range(1, 100, 7):
        if i % 11 == 0:
            print(i)
            break

# stop_at_11()


def print_div_3and5():
    for i in range(0, 21):
        if i % 3 != 0 and i % 5 != 0:
            print(i)


print_div_3and5()