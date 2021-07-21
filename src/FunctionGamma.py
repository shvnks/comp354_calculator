from FunctionBase import FunctionBase
from FunctionExponent import FunctionExponent
from CalculationErrorException import CalculationErrorException

class FunctionGamma(FunctionBase):

    g = 7
    lanczos_coef = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7]

    def gamma(z):
        z = complex(z)
        if z.real < 0.5:
            return FunctionBase. / (sin(pi*z)*gamma(1-z))
        else:
            z -= 1
            x = lanczos_coef[0]
            for i in range(1, g+2):
                x += lanczos_coef[i]/(z+i)
            t = z + g + 0.5
            return sqrt(2*pi) * t**(z+0.5) * exp(-t) * x
