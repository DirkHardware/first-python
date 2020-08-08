class Kettle(object):

    # This attribute will be universal to all instances of kettle
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True
        print("Your {0.make} is on!".format(self))

    def switch_off(self):
        self.on = False
        print("Your {0.make} is off!".format(self))


hamilton = Kettle("Hamilton", 14.55)
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)
print(kenwood.power_source)
print(hamilton.power_source)

# Object variables are called attributes
# The creation of a class instance is called instantiation
# print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

kenwood.switch_on()
hamilton.switch_on()
# You can also do it like this, by manually supplanting the self argument
Kettle.switch_off(kenwood)

# You can also dynamically assign attributes to instances
kenwood.power = 1.5
print(kenwood.power)

# You can turn objects into dictionaries
print(Kettle.__dict__)
print(hamilton.__dict__)