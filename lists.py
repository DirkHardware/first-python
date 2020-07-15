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