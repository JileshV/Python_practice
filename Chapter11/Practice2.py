class Animals:
    a = "Animal"

class Pets(Animals):
    p = "Pet"

class Dog(Pets, Animals):
    d = "Dog"
    def bark(self):
        print(f"{self.d} is a {self.p} {self.a}")

c1 = Dog()
c1.bark()