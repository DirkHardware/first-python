chapters = [
    "Ultramarines",
    "Blood Angels",
    "Imperial Fists",
    "Black Templars",
    "White Scars",
]

# SORTING LISTS

chapters.sort()
print(chapters)

# Sort arranges thing by alphanumeric order
# Sort has two key arguments. The first is reverse, which function is obvious

chapters.sort(reverse=True)
print(chapters)

# THERE ARE TWO SORT FUNCTIONS
# sort() modifies a list, while sorted() creates a new list, and as
# such can be used on immutable objects

totd = "Heresy grows from idleness"
letters = sorted(totd)
print(letters)

# Note that sorted() is a function while sort() is a method

# CASE INSENSITIVE SORTING

callback = sorted("Fear me. BUT FOLLOW!",
                  key=str.casefold)
# We don't want to use parens here because we're not trying to call the function
# We're merely telling the sorted function what function it should use to compare
# the values

sorted_list = sorted("a StRiNg", key=str.lower)
print(sorted_list)