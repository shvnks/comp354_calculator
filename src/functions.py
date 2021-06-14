# make your functions here
import math


def exponent_function(constant, base, power):

    total = base

    if power % 1 == 0:
        if power == 0 or power == -0:
            return constant * 1
        if power > 0:
            counter = power - 1
            while counter > 0:
                total *= base
                counter -= 1
            return constant * total
        else:
            power *= -1
            counter = power - 1
            while counter > 0:
                total *= base
                counter -= 1
            total = 1 / total
            return constant * total
    elif power % 1 != 0:
        if power == 0 or power == -0:
            return constant * 1
        if power > 0:
            sqrt = base ** power
            return constant * sqrt
        else:
            power *= -1
            sqrt = 1 / (base ** power)
            return constant * sqrt

# print("\nPOSITIVE WHOLE NUMBERS")
# print("2^0= " + str(exponent_function(1, 2, 0)))
# print("2^1= " + str(exponent_function(1, 2, 1)))
# print("2^2= " + str(exponent_function(1, 2, 2)))
# print("2^3= " + str(exponent_function(1, 2, 3)))
# print("1^4= " + str(exponent_function(1, 1, 4)))
#
# print("\nNEGATIVE WHOLE NUMBERS")
# print("2^-0= " + str(exponent_function(1, 2, -0)))
# print("2^-1= " + str(exponent_function(1, 2, -1)))
# print("2^-2= " + str(exponent_function(1, 2, -2)))
# print("2^-3= " + str(exponent_function(1, 2, -3)))
# print("1^-4= " + str(exponent_function(1, 1, -4)))
#
# print("\nPOSITIVE FLOAT NUMBERS")
# print("2^0.0= " + str(exponent_function(1, 2, 0.0)))
# print("2^0.5= " + str(exponent_function(1, 2, 0.5)))
# print("2^1.5= " + str(exponent_function(1, 2, 1.5)))
# print("2^2.5= " + str(exponent_function(1, 2, 2.5)))
# print("2^3.5= " + str(exponent_function(1, 2, 3.5)))
# print("1^4.5= " + str(exponent_function(1, 1, 4.5)))
# print("4^1.5= " + str(exponent_function(1, 4, 1.5)))
# print("8^0.3= " + str(exponent_function(1, 8, 0.3)))
# print("2^arcos(0.98)= " + str(exponent_function(1, 2, math.acos(0.98))))
# print("2^log2(10)= " + str(exponent_function(1, 2, math.log(10, 2))))

# print("\nNEGATIVE FLOAT NUMBERS")
# print("2^-0.0= " + str(exponent_function(1, 2, -0.0)))
# print("2^-0.5= " + str(exponent_function(1, 4, -0.5)))
# print("2^-1.5= " + str(exponent_function(1, 2, -1.5)))
# print("2^-2.5= " + str(exponent_function(1, 2, -2.5)))
# print("2^-3.5= " + str(exponent_function(1, 2, -3.5)))
# print("1^-4.5= " + str(exponent_function(1, 1, -4.5)))
# print("4^-1.5= " + str(exponent_function(1, 4, -1.5)))
# print("8^-0.3= " + str(exponent_function(1, 8, -0.3)))
