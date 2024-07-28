""" 
    LISKOV SUBTITUTION:
        Functions that use pointers or references to 
        base classes must be able to use objects of
        derived classes without knowing it
"""
class Vehicle:
    def accelerate(self):
        pass

    def brake(self):
        pass

class Car(Vehicle):
    def accelerate(self):
        print("Car is accelerating")

    def brake(self):
        print("Car is braking")

class Motorcycle(Vehicle):
    def accelerate(self):
        print("Motorcycle is accelerating")

    def brake(self):
        print("Motorcycle is braking")

"""
    WHEN WE ARE CALLING TO FATHER CLASS TO DO
    THE TESTS, WE CAN USE DIFFERENTS CHILD
    CLASSES.
"""

def test_vehicle(vehicle):
    vehicle.accelerate()
    vehicle.brake()

# Usage
car = Car()
motorcycle = Motorcycle()

test_vehicle(car)
test_vehicle(motorcycle)