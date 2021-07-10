
from abc import ABC, abstractmethod

# FunctionBase: Base class used to for the custom math functions
class FunctionBase(ABC):
    #constructor: initialize the class, takes in the values that will be used to evaluate the function
    def __init__(self) -> None:
        super(ABC, self).__init__()
        self.MAX_TERMS = 100
        pass

    # calculateEquation: Method that will be called to calculate the math function
    @abstractmethod
    def calculateEquation(self) -> float:
        raise NotImplementedError()