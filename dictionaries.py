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
