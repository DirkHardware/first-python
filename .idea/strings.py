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

print(letters[-4:]) #get the last 4 characters of any string.


#slicing in steps, seperator example

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])


# % interpolation
# print("%s %s %s" %('Hello','World', 'I am Satan.'))

# Multiplying strings
# shootin = "Dakka "
#
# print (shootin * 5) #"Dakka Dakka Dakka Dakka Dakka"
#
# print ("Dak" in shootin) #True
# print ("ka " in shootin) #True
# print ("Chop" in shootin) #False

#Repfields
print("Repfields\n")
age = 24
print("My age is " +str(age) + " years")
#see also
print("My age is {0} years".format(age))
#or
tens = "two"
singles = "four"
print("My age is {0} and {1} years".format(tens,singles))

#String Formatting
category = "String Formatting"
print(f"\n\n{category}\n ")
#bad formatting, numbers don't line up
print("Bad formatting, numbers don't line up.")
for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
print("\n\nGood formatting. Number to right of replacement index determines no. of characters in replacement space.\n")
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
#force left aliginment
print("\n\nForce left alignment\n")
for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
#fstrings and other formatting
print("\n\nf strings\n")
pi = 22/7
print(f"Pi is approximately {pi:12.50f}") #formats pie

if(1 == 1):
    print("florp")