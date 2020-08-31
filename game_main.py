from game_player import Player

anderson = Player("Anderson")

print(anderson.name)
print(anderson._lives)
print(anderson.score)
anderson._lives -= 1
print(anderson._lives)



