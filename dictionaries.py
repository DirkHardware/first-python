# So it looks like dictionaries work the same way as hashs or objects,
# Except the keys cannot be string literals if they are not in quotes

factions = {"Space Marines": "Assholes with giant shoulder pads",
            "Orks": "Cockney Space Hooligans",
            "Tyranids": "The bugs from Alien",
            "Imperial Guard": "The true heroes of the Imperium",
            7: 8}

# Heres how you access individual items

faction_details = factions["Imperial Guard"]
print(faction_details)

# Updating a value
factions["Space Marines"] = "Spehss Muhrines"

print(factions)

# Getting rid of a key/value pair
del factions[7]

print(factions)

# To clear out the whole dictionary
# factions.clear()
# print(factions)

# Watch out when calling values by their keys. A non extant key will
# throw an error. A better way to call them is by the .get() method
# which will not throw an error
# print(factions["Grey Knights"])

# print(factions.get("Grey Knights"))

# .get() can also take a default value to return if the key isn't in the dictionary
# Example below

# while True:
#     dict_key = input("Please enter a faction: ")
#     if dict_key == "quit":
#         break
#     description = factions.get(dict_key, "There are no {0} in the 41st millenium".format(dict_key))
#     print(description)

# Dictionaries are obviously iteratable
# However it is not guaranteed that they will show up in the same order
for faction in factions:
    print(factions[faction])