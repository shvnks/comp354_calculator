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
            tokens = readchars.createTokens()

            # print(list(tokens))

            mathEXP = CreateExpression(tokens)
            tree = mathEXP.readTokens()

            print(tree)

            expression = EvaluateExpression(tree)
            print(f"Result: {expression.getResult()}")

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
    print('\u03c0')
    print('\u221a')
    print('\u03c3')
    print('\u0393')
    print('\u03c3[10,8,6]')
    main(sys.argv)
