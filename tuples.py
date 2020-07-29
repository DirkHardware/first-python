#TUPLES! FUCKING FINALLY!

# A tuple is a mathematical name for an ordered set of data

# Tuples differ from lists because tuples are immutable. That means
# they can't be changed after they've been created - like strings.
# Apparently the upshot of this is because you don't need the overhead
# of methods that a list has, they save memory.

# All sequence operations can be performed on Tuples
# Apparently they're also useful for guarding against unintended changes
# especially when dealing with databases.

t = ("a", "b", "c")
print(t)

# Parenthesis must be used on tuples when passing them as an argument

samurai = ("Seven Samurai", "Akira Kurosawa", 1954)
max = ("Mad Max", "George Miller", 1979)
aliens = ("Aliens", "James Cameron", 1986)
ghost = ("Ghost World", "Terry Zwigoff", 2001)
print(samurai[0])
print(samurai[1])

# To convert a tuple to a string

samurai_list = list(samurai)
print(samurai_list)