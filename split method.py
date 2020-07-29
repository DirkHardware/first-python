# Split is a string method that a string and
# generates a list of its component words.

creed = "The Emperor Protects"
words = creed.split()

print(words)

# The split method seperates along one or more whitespaces by default
# but can take any string as a seperator

creed = "ThehurfEmperorhurfProtects"
words = creed.split("hurf")

print(words)