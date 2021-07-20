from FunctionBase import FunctionBase
from FunctionExponent import FunctionExponent
from CalculationErrorException import CalculationErrorException


class FunctionMad(FunctionBase):

    # constructor
    def __init__(self, *argument) -> None:
        super(FunctionMad, self).__init__()
        self.argument = argument


def calculateEquation(self) -> float:

    # calculating the mean of inputs
    mean = 0
    for i in range(0, self.arguments.length):
        mean += self.arguments[i]
    mean = mean/self.arguments.length
    deviation = 0
    summ = 0
    for i in range(0, self.arguments.length):
        deviation = self.arguments[i]-mean
    if deviation < 0:
        deviation = -deviation
    summ += deviation
    return summ / self.arguments.length
