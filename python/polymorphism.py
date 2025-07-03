class Animal:
    def make_sound(self):
        return "make a generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Dog Barks!"

class Cat(Animal):
    def make_sound(self):
        return "Cat Meows"

class Cow(Animal):
    def make_sound(self):
        return "Cow Moos"

def make_animal_sound(animal_obj):
    print(animal_obj.make_sound()) 
    # print(animal_obj.make_sound) # Call the method to get the sound

# Create instances of each animal outside of the class definitions
c1 = Cat()
d1 = Dog()
C1 = Cow()

# Make sounds for each animal
make_animal_sound(c1)
make_animal_sound(d1)
make_animal_sound(C1)
