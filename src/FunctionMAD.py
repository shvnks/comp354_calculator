from FunctionBase import FunctionBase
from FunctionExponent import FunctionExponent
from CalculationErrorException import CalculationErrorException


class FunctionMad(FunctionBase):

    # constructor
    def __init__(self, arguments: list) -> None:
        super(FunctionMad, self).__init__()
        self.arguments = arguments


def calculateEquation(self) -> float:

    # calculating the mean of inputs
    mean = 0
    for i in range(0, len(self.arguments)):
        mean += self.arguments[i]
    mean = mean/len(self.arguments)
    deviation = 0
    summ = 0
    for i in range(0, len(self.arguments)):
        deviation = self.arguments[i]-mean
    if deviation < 0:
        deviation = -deviation
    summ += deviation
    return summ / len(self.arguments)
