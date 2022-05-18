class Bird():

    def __init__(self, name):
        self.name = name
        self._walk = f'{self.name} bird can walk'

    def fly(self):
        try:
            print(self._fly)
        except AttributeError:
            print(f"AttributeError: {self.name} object has no attribute 'fly'")

    def walk(self):
        print(self._walk)

    def __str__(self):
        return f'{self.name} bird can walk'


class FlyingBird(Bird):

    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration
        self._fly = f'{self.name} bird can fly'

    def eat(self):
        print(f'It eats mostly {self.ration}')

    def __str__(self):
        return f'{self.name} bird can fly and walk'


class NonFlyingBird(Bird):

    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.ration = ration
        self._swim = '{} bird can swim'.format(self.name)

    def swim(self):
        print(self._swim)

    def __str__(self):
        return f'{self.name} bird can swim'

    def eat(self):
        print(f'It eats mostly {self.ration}')


class SuperBird(NonFlyingBird, FlyingBird, Bird):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'{self.name} bird can swim, fly and walk'


b = Bird("Any")
b.walk()

c = FlyingBird("Canary")
str(c)
c.eat()

p = NonFlyingBird("Penguin", "fish")
p.swim()
p.fly()
p.eat()

s = SuperBird("Gull")
str(s)
s.eat()

print(SuperBird.__mro__)