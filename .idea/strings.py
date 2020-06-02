parrot = "Norwegian Blue"

#slicing
print (parrot[0:6]) #Norweg
print (parrot[:9]) #Norwegian
print (parrot[10:]) #Blue

print(parrot[:6] + parrot[6:]) #Norwegian Blue

print(parrot[:]) #Norwegian Blue

print(parrot[-14:-8]) #Norweg
print(parrot[-14:]) #Norwegian Blue

#slicing in steps
print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Nw

number = "9,223,372,036,854,775,807"
print(number[1::4]) #,,,,,,

#negative slicing

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1]
print(backwards)

backwards_slice = letters[25:16:-1]
# or
backwards_slice2 = letters[:-9:-1]
print(backwards_slice)


#slicing in steps, seperator example

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])


# % interpolation
# print("%s %s %s" %('Hello','World', 'I am Satan.'))
