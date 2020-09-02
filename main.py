from player import Player

anderson = Player("Anderson")

print(anderson.name)
# print(anderson.lives)
# anderson.lives -= 1
# print(anderson)
#
# anderson.lives -= 1
# print(anderson)
#
# anderson.lives -= 1
# print(anderson)
#
# anderson.lives -= 1
# print(anderson)

anderson.level = 5
print(anderson.level)
print(anderson.score)

anderson.level = 2
print(anderson.level)
print(anderson.score)

anderson.level = 1
print(anderson.level)
print(anderson.score)

anderson.level = 0
