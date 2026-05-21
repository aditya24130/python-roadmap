class Animal:

    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def __init__(self, name, breed):

        
        super().__init__(name)

        self.breed = breed


    def sound(self):
        print("Dog barks")


d1 = Dog("Tommy", "Labrador")

print("Name:", d1.name)
print("Breed:", d1.breed)

d1.sound()