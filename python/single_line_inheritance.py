class Animal:
    def __init__(self,name):
        self.name=name
        print({self.name},"the name of the animal")

#method
    def speak(self):
        print("A Generic sound which an animal makes")
class Dog(Animal):
    def __init__(self,name,breed,color):
        super().__init__(name)
        self.breed=breed
        self.color=color

    #behaviours of dog
    def Make_sound(self):
        print("DOG BARKS!!")

Dog1=Dog("leo","husky", "red")            
Dog1.speak()
