
class Animal:

    def __init__(self, name, age,race, size):
        """
        @:parameter
        """
        self.name = name
        self.age = age
        self.race = race
        self.size = size

    def __getattr__(self):
        return self.size

class Dog(Animal):
    pass

class Cat(Animal):
    pass

if __name__ == '__main__':

    dog = Dog("Dingo", 15, "Pastore Tedesco", "Media")
    cat = Cat("Gatto", 17, "Alla Vicentina", "Piccola")
    print(dog.__getattr__())
    print(cat.__getattr__())