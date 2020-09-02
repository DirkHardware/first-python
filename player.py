class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, new_level):
        if new_level > 0:
            # if new_level > self._level:
            score_bonus = new_level - self._level
            self._level = new_level
            self._score = self._score + (1000 * score_bonus)
            # It turns out I didn't need this part. If the level had gone down
            # the score_bonus would be negative
            # elif new_level < self._level:
            #     score_bonus = self._level - new_level
            #     self._level = new_level
            #     self.score = self.score - (1000 * score_bonus)
        elif new_level < 1:
            print("Level cannot be less than 1 ")
            self._level = 1
            self._score = 0

    # This line allows the .lives values in main.py to work as they are
    # written without rewriting or calling the setter and getter functions
    #
    # In fact, you can see we can use properties to affect anything as long
    # as we have getter and setter methods
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # ALTERNATE PROPERTY SYNTAX

    # These @comments are called decorators. They are an alternative syntax
    # The @property method marks score as a property while the @score.setter indicates
    # the following method is a setter. This obviates binding a property to a variable
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    # This use of the string functions returns this string whenever an instance of the class
    # is used as an argument in a print function
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)


if __name__ == '__main__':
    print('test')