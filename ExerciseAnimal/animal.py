class Animal:

    @classmethod
    def move(cls):
        if cls.__name__ == "Dog":
            print("Dog is moved!")
        elif cls.__name__ == "Lion":
            print("Lion is moved!")
        elif cls.__name__ == "Mouse":
            print("Mouse is moved!")
        elif cls.__name__ == "LadyBug":
            print("LadyBug is moved!")
        elif cls.__name__ == "Zebra":
            print("Zebra is moved!")
        else:
            print("Animal is moved!")

class Dog(Animal):
    pass

class Lion(Animal):
    pass

class Mouse(Animal):
    pass

class LadyBug(Animal):
    pass

class Zebra(Animal):
    pass