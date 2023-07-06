"""
    DEPENDENCY INVERSION:
        Abstractions should not depend on details.
        Details should depend on abstraction.
        High-level modules should not depend on low-level modules.
        Both should depend on abstractions
"""
from abc import ABC, abstractmethod

class CalculatorInterface(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

class Calculator(CalculatorInterface):
    def add(self, a, b):
        return a + b

class App:
    def __init__(self, calculator: CalculatorInterface):
        self.calculator = calculator

    def perform_calculation(self, a, b):
        result = self.calculator.add(a, b)
        print(f"The result is: {result}")

"""
    THE APP CLASS DEPEND ON THE ABSTRACTION
    RATHER THAN THE CONCRETE IMPLEMENTATION.
    
    WITH THIS THE APP CLASS IS MORE FLEXIBLE
    AND REUSABLE.
"""

calculator = Calculator()
app = App(calculator)
app.perform_calculation(5, 3)