from CharacterReader import charReader
from InterpreterErrors import UnknownElementError, NoExpression, TooManyDecimalsException, MissingParenthesisException, SyntaxException
from CreateExpression import CreateExpression
from ComputeExpression import EvaluateExpression

class Interpreter:
    def __init__(self, equation:str) -> None:
        self.equation = equation

    def isValid(self) -> tuple[bool, str]:

        try:

            readchars = charReader(self.equation)
            tokens = readchars.create_Tokens()
            mathEXP = CreateExpression(tokens)
            tree = mathEXP.read_Tokens()
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
        except NoExpression:
            pass

        return (True, 'No Error')

    def evaluateEquation(self) -> tuple[float, bool, str]:

        try:

            readchars = charReader(self.equation)
            tokens = readchars.create_Tokens()
            mathEXP = CreateExpression(tokens)
            tree = mathEXP.read_Tokens()
            expression = EvaluateExpression(tree)
            result = expression.get_Result()

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
        except NoExpression:
            pass

        return (result, True, 'No Error')
