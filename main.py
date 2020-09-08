from player import Player
from enemy import Enemy, Troll, Vampyre

anderson = Player("Anderson")

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

lazlo = Vampyre("Lazlo")
nandor = Vampyre("Nandor")

print(lazlo)
print(nandor)

lazlo.take_damage(9)
nandor.take_damage(13)
brother.take_damage(22)
another_troll.take_damage(24)

print(lazlo)
print(nandor)
print(brother)
print(another_troll)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

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
