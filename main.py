from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

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

print(lazlo)
print(nandor)
print(brother)
print(another_troll)

max = VampyreKing("Max")

# while lazlo._alive:
#     lazlo.take_damage(1)
#         # print(lazlo)

while max._alive:
    max.take_damage(4)


# print(anderson.name)
# print(anderson._lives)
# anderson._lives -= 1
# print(anderson)
#
# anderson._lives -= 1
# print(anderson)
#
# anderson._lives -= 1
# print(anderson)
#
# anderson._lives -= 1
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
