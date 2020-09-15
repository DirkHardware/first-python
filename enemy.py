import random


class Enemy:

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points and have {} left ".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    # Refactor doesn't work on strings in the __str__ method 
    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name, status="Fine"):
        # One way of calling the init method from the super class, this is the python 2 way
        # Enemy.__init__(self, name=name, _lives=1, _hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)
        # Any attributes beyond those passed down by the super can be added afterwards
        self.status = status

    def grunt(self):
        print("Me {0._name}. {0.name} stomp you.".format(self))

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points} Status:{0.status}".format(self)


class Vampyre(Enemy):

    def __init__(self, name, status="Spooky"):
        # For whatever bizarre reason, you have to keep name=name even when you change
        # the attribute to _name in the superclass
        super().__init__(name=name, lives=3, hit_points=12)
        self.status = status

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodges *****".format(self))
            return True
        else:
            return False

    # overrides the superclass version
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points} Status:{0.status}".format(self)

class VampyreKing(Vampyre):

    # This is my solution. For some reason I can't seem to use the init super method the same way the
    # regular Vampyre Class does
    def __init__(self, name, status="V. Spook"):
        super().__init__(name=name)
        # Because the above line is actually creating a new Vampyre instance we can't
        # just change the variables via the super init apparently. We have to add them manually
        self._lives = 3
        self._hit_points = 140

    def take_damage(self, damage):
        # if not self.dodges():
        #     super().take_damage(damage=damage/4)
        # Time's way is better
        super.().take_damage(damage // 4)

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points} Status:{0.status}".format(self)



