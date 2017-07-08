import random

class Greeter(object):
    def __init__(self,name):
        self.name = name

    def hello(self):
        print("hello " + self.name)

    def goodbye(self):
        print("goodbye " + self.name)


class Die(object):
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        return random.randint(1, self.sides)

d = Die(3)
print(d.roll())
print(d.roll())
print(d.roll())

d2 = Die(1000000)
print(d2.roll())
print(d2.roll())
print(d2.roll())


g = Greeter("tata swinka")
#g.hello()
#g.goodbye()

g2 = Greeter("george")
#g2.hello()
#g2.goodbye()
