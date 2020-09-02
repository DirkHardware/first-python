class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self.level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        self._lives = lives

    # This line allows the .lives values in main.py to work as they are
    # written without rewriting or calling the setter and getter functions
    lives = property(_get_lives, _set_lives)


if __name__ == '__main__':
    print('test')