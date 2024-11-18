class Animal:
    def __init__(self):
        pass

    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return 'woof woof'

class Cat(Animal):
    def talk(self):
        return 'meow'


def func(animal):
    print(animal.talk())

cat = Cat()
dog = Dog()
func(cat)
func(dog)
