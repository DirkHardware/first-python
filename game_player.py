class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self.level = 1
        self.score = 0

    # because _lives is hidden with an underscore, we need to create
    # getter and setter methods for it

    def _get_lives(self):
        return self._lives


    def _set_lives(self, lives):
        self._lives = lives

    lives = property(_get_lives, _set_lives)



