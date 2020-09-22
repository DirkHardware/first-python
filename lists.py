import random

chapters = [
    "Ultramarines",
    "Blood Angels",
    "Imperial Fists",
    "Black Templars",
    "White Scars",
]

# Lists, which should be called arrays, work the same way they do in JS
# and Ruby. The key difference is that you can use the same iteration
# syntax used in strings on lists.

# Slice of tirst three chapters
print(chapters[0:2])

# The first chapter and every other chapter afer
print(chapters[0::2])

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(odd))

print('Kashyyk'.count('y'))

# ITERATING OVER A LIST

# for chapter in chapters:
#     print("chapter {0}: {1}".format(chapters.index(chapter) + 1, chapter))

# The emumerate function is a better way to handle this

# for index, chapter in enumerate(chapters):
#     print("chapter {0}: {1}".format(index + 1, chapter))

# index doesn't have to be called index, the variables between for and in
# can be called whatever

# REMOVING ITEMS FROM LISTS

traitor_legions = ["Black Legion",
                   "Alpha Legion",
                   "Death Guard",
                   "Emperor's Children",
                   "Night Lords",
                   "Thousand Suns"]

rand_legion = random.randint(1, len(traitor_legions)) - 1
print(rand_legion)

chapters.append(traitor_legions[rand_legion])
# print(chapters)

for chapter in chapters:
    if chapter in traitor_legions:
        print("Uh oh! There's a traitor in our midst! Looks like it's the {0}".format(traitor_legions[rand_legion]))
        chapters.remove(chapter)
    else:
        print(chapter)

# print("""\n \n {0}""".format(chapters))

# ADDING ONE LIST TO ANOTHER

chapters.extend(traitor_legions)
# Note that it doesn't sort, and instead works like concat on a string
# print(chapters)

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

# CONCATANATING LISTS

all_chapters = chapters + traitor_legions
print(all_chapters)

different_chapters = ["Scorpions", "Salamanders"]
updated_chapters = chapters
updated_chapters[2:] = different_chapters
print(updated_chapters)

# the list() class constructor can also be used to make a list out of any iterable

# list("4321")

# COPYING LISTS

# You can also copy lists with slices
more_chapters = chapters[:]
print(more_chapters)

# A really effecient way is with the .copy() method
more_chapters = chapters.copy()
print(more_chapters)

# DELETING LISTS

# delete slices of data with the del function
data = ["Jim", "Bob", "Khorne", "Nurgle", "Tzeench", "Slaanesh"]
del data[0:2]
print(data)

# Be careful deleting items in a list as you iterate *forward* over it. In the
# example below, 5 and 598 are not deleted, because when the for loop
# hits 1 and 101 respectively, when the loop deletes the items at their
# index, thus causing 5 and 598 to each move down an index. When the
# for loop moves on to the next index, it skips them, because 20 and the
# list and now occupy their old spaces due to the index shift
# caused by the deletions.
#
min_valid = 10
max_valid = 100
data = [1, 5, 20, 48, 64, 101, 598]
#
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#
# print(data)

# The safe way to strip the low values is shown bellow
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

# To strip the high values:
start = 0
# startimg backwards
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break
print(start)
del data[start:]
print(data)

# You can also just iterate BACKWARDS!

data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# for index in range(len(data) -1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]
# print(data)

# Reverse function
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        # What printing the index in a reversed enumerator shows is
        # just the number of steps backwards taken. You have to subtract
        # index from top_index to get the real index of each enumrated
        # value
        true_index = top_index - index
        print(true_index, value)
        print(data)
        del data[true_index]
print(data)

# Quick update