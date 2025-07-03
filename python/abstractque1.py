# Create an abstract class Vehicle with an abstract method start_engine(). Then, create two child classes Car and Bike that implement this method with their own message like "Car engine started" and "Bike engine started".
# Demonstrate usage by creating objects and calling start_engine().
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):

    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):

    def start_engine(self):
        print("Bike engine started")

car = Car()
car.start_engine()

bike = Bike()
bike.start_engine()

