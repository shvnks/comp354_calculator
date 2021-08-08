import math

import FunctionFactorial
import FunctionExponent
import FunctionGamma
import FunctionLog
import FunctionSinh
import FunctionArccos
import FunctionStandardDeviation
import FunctionMAD

def main() -> None:

    rounding = 9

    factorialList = [0, 1, 2, 3, 4, 5, 6]
    for i in factorialList:
        a = FunctionFactorial.FunctionFactorial(i).calculateEquation()
        b = math.factorial(i)
        if a != b:
            raise Exception('Factorial: %f not equal to %f for i = %f' % (a, b, i))

    exponentList = [[0,0], [0,1], [1,0], [1,1], [2,5], [8,0.5], [1.5,1.567], [4,-3], [4,-2.456], [4.567,-1.234]]
    for x, y in exponentList:
        a = FunctionExponent.FunctionExponent(x, y).calculateEquation()
        b = round(x ** y, rounding)
        if str(a) != str(b):
            raise Exception('Exponent: %.10f not equal to %.10f for x = %.10f, y = %.10f' % (a, b, x, y))

    sinhList = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
    for i in sinhList:
        a = FunctionSinh.FunctionSinh(i).calculateEquation()
        b = round(math.sinh(i), rounding)
        if a != b:
            raise Exception('Sinh: %.10f not equal to %.10f for i = %.10f' % (a, b, i))
            

    logList = [[2,3], [3,4], [4,5.6], [7.3,4.6], [10.5,2]]
    for b, n in logList:
        a1 = FunctionLog.FunctionLog(b, n).calculateEquation()
        a2 = round(math.log(n, b), rounding)
        if a1 != a2:
            raise Exception('log: %.10f not equal to %.10f for b = %.10f, n = %.10f' % (a1, a2, b, n))


    stddevList = [[1, 2, 4, 5], [1.2, 7.5, 3.6, 1.3, 1.765]]
    stddevExpectedResults = [1.5811388300, 2.3764923740]
    for l, r in zip(stddevList, stddevExpectedResults):
        a1 = FunctionStandardDeviation.FunctionStandardDeviation(l).calculateEquation()
        a2 = r
        if a1 != a2:
            raise Exception('Std Dev: %.10f not equal to %.10f for list = %s' % (a1, a2, l))


    madList = [[1, 2, 4, 5], [1.2, 7.5, 3.6, 1.3, 1.765]]
    MADExpectedResults = [1.5, 1.9816]
    for l, r in zip(madList, MADExpectedResults):
        a1 = FunctionMAD.FunctionMAD(l).calculateEquation()
        a2 = r
        if a1 != a2:
            raise Exception('MAD: %.10f not equal to %.10f for list = %s' % (a1, a2, l))

    gammaList = [-1.5, -0.4, 1.5, 2]
    gammaExpectedResults = [2.36327180152582, -3.722976008521843, 0.886226925, 0.999998185]
    for i, r in zip(gammaList, gammaExpectedResults):    
        a1 = FunctionGamma.FunctionGamma(i).calculateEquation()
        a2 = r
        if a1 != a2:
            print('Gamma: %s not equal to %s for i = %.10f' % (str(a1), str(a2), i))

    arccosList = [-0.6, -0.3, -0.2, 0, 0.2, 0.3, 0.6]
    arccosExpectedResult = [2.214297, 1.8754890, 1.772154, 1.570796, 1.369438, 1.266103, 0.927295]
    for i, r in zip(arccosList, arccosExpectedResult):
        a1 = FunctionArccos.FunctionArccos(i).calculateEquation()
        a2 = r
        if a1 != a2:
            print('Arccos: %.10f not equal to %.10f for i = %.10f' % (a1, a2, i))



if __name__ == "__main__":
    main()