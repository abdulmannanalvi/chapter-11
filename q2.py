class Animal:
    pass
class Pet(Animal):
    @staticmethod
    def bark():
        print("Bow Bow!")
class Dog(Pet):
    pass

a=Dog()
a.bark()
    