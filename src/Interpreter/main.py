"""Expression Parsing with an Interpreter."""
from CharacterReader import charReader
from InterpreterErrors import UnknownElementError, NoExpression, TooManyDecimalsException, MissingParenthesisException, SyntaxException
from CreateExpression import CreateExpression
from ComputeExpression import EvaluateExpression
import sys


def main(argv):
    """Run Main Function."""
    # While the User wants to still compute expressions
    while True:

        try:
            user_input = input('>>> ')

            readchars = charReader(user_input)
            tokens = readchars.create_Tokens()

            mathEXP = CreateExpression(tokens)
            tree = mathEXP.read_Tokens()

            expression = EvaluateExpression(tree)
            print(f"Result: {expression.get_Result()}")

        # List of Errors the interpreter can arrive at. Errors can be understood by their names, or their print statements
        except TooManyDecimalsException as T:
            print(str(T))
        except UnknownElementError as U:
            print(str(U))
        except MissingParenthesisException as M:
            print(str(M))
        except SyntaxException as S:
            print(str(S))
        except ZeroDivisionError:
            print('MATH ERROR: Divide by Zero')
        except NoExpression:
            pass


if __name__ == '__main__':
    main(sys.argv)
