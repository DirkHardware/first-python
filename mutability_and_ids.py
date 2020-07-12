
chapters = [
    "Ultramarines",
    "Blood Angels",
    "Imperial Fists",
    "Black Templars",
    "White Scars",
]

more_chapters = chapters
print(id(chapters))
print(id(more_chapters))

chapters += ["Lamenters"]
# chapters.append("Lamenters") also works
print(chapters)
print(id(chapters))


# Look! No matter what the fuck you do the list, the id remains the same!
# Because its *mutable*!

print(more_chapters)
print(id(more_chapters))

# And looK! more_chapters is changed as well, yet the id remains.

