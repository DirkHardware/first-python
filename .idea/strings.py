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