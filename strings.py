# Slicing
parrot = "Norwegian Blue"

# [Start:Stop] Last character isn't included in the slice.
print(parrot[0:6]) # Norweg
# [Start:Stop:Step] Start and stop values left blank are implicitly set to beginning and end respectively
print(parrot[:8:2]) # Nrei
print(parrot[9::2]) #  le


# number = "9,223;372:0366 054,755;807"
# separators = number[1::4]
