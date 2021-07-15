from FunctionFactorial import FunctionFactorial

#constants
PI = 3.1415926535897932384626433
MAX_RESULT = 10000000
MIN_RESULT = -10000000
#main funciton
def sinh(num, isDeg=False):
    if(isDeg):
        num = num * PI/180
    
    num1 = custom_exp(num)
    num2 = custom_exp(-num)

    result = (num1-num2)/2

    if(result > MAX_RESULT):
        raise Exception("result too large")
    elif(result < MIN_RESULT):
          raise Exception("result too small")      

    return result


#helper functions
def custom_factorial(n):
    result=1
    if n==0:
        return 1
    elif n>0:
        for i in range(1,n+1):
            result = result*i
        return result
    

def custom_exp(x):
    n=0
    for i in range(0, 100):
      n= n + (x**i)/custom_factorial(i)
    return n


print(sinh(100))
