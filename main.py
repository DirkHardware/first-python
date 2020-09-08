from player import Player
from enemy import Enemy

anderson = Player("Anderson")
random_monster = Enemy("Baisc enemy", 12, 1)

print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

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
