"""Expression Parsing with an Interpreter."""
from CharacterReader import charReader
from InterpreterErrors import UnknownElementError, NoExpression
from CreateExpression import CreateExpression
from ComputeExpression import EvaluateExpression


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
    except ValueError:
        print('SYNTAX ERROR')
    except UnknownElementError as U:
        print(f'Unknown Symbol: {U.element}')
    except ZeroDivisionError:
        print('MATH ERROR')
    except NoExpression:
        pass
