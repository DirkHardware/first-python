from player import Player
from enemy import Enemy, Troll

anderson = Player("Anderson")

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

# print(anderson.name)
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

# anderson.level = 5
# print(anderson.level)
# print(anderson.score)
#
# anderson.level = 2
# print(anderson.level)
# print(anderson.score)
#
# anderson.level = 1
# print(anderson.level)
# print(anderson.score)
#
# anderson.level = 0
#
# anderson.score = 500
# print(anderson)
