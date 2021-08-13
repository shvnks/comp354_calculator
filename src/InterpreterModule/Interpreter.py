from CharacterReader import charReader
from InterpreterErrors import UnknownElementError, NoExpression, TooManyDecimalsException, MissingParenthesisException, SyntaxException
from CreateExpression import CreateExpression
from ComputeExpression import EvaluateExpression
from CalculationErrorException import CalculationErrorException

class Interpreter:
    def __init__(self, equation:str) -> None:
        self.equation = equation

    def isValid(self) -> tuple[bool, str]:

        try:

            readchars = charReader(self.equation)
            tokens = readchars.createTokens()
            mathEXP = CreateExpression(tokens)
            tree = mathEXP.readTokens()
            expression = EvaluateExpression(tree)

        except TooManyDecimalsException as T:
            return (False, str(T))
        except UnknownElementError as U:
            return (False, str(U))
        except MissingParenthesisException as M:
            return (False, str(M))
        except SyntaxException as S:
            return (False, str(S))
        except ZeroDivisionError:
            return (False, 'MATH ERROR: Divide by Zero')
        except CalculationErrorException as C:
            return (False, str(C))
        except NoExpression:
            pass

        return (True, 'No Error')

    def evaluateEquation(self, isDeg:bool) -> tuple[float, bool, str]:

        result = 0.0
        try:

            readchars = charReader(self.equation)
            tokens = readchars.createTokens()
            mathExp = CreateExpression(tokens)
            tree = mathExp.readTokens()
            expression = EvaluateExpression(tree)
            result = expression.getResult(isDeg)

        except TooManyDecimalsException as T:
            return (None, False, str(T))
        except UnknownElementError as U:
            return (None, False, str(U))
        except MissingParenthesisException as M:
            return (None, False, str(M))
        except SyntaxException as S:
            return (None, False, str(S))
        except ZeroDivisionError:
            return (None, False, 'MATH ERROR: Divide by Zero')
        except CalculationErrorException as C:
            return (None, False, str(C))
        except NoExpression:
            pass

        return (result, True, 'No Error')
