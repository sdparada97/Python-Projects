"""
    INTERFACE SEGREGATION:
        Many client-specific interfaces are better than
        one general-purpose interface
"""
from abc import ABC, abstractmethod

class Walker(ABC):
    @abstractmethod
    def walk() -> bool:
        return print("Can Walk") 

class Swimmer(ABC):
    @abstractmethod
    def swim() -> bool:
        return print("Can Swim") 

class Human(Walker, Swimmer):
    def walk():
        return print("Humans can walk") 
    def swim():
        return print("Humans can swim") 

class Whale(Swimmer):
    def swim():
        return print("Whales can swim") 

"""
    THIS PRODUCE THAT CLASSES DONT HAVE ABTRACTS 
    WRONG ABOUT BEHAVIOR Y ABSTRACTION.
"""

if __name__ == "__main__":
    Human.walk()
    Human.swim()

    Whale.swim()
    Whale.walk()