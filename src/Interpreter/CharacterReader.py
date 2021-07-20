"""Reads math expression one character at a time."""
from InterpreterErrors import UnknownElementError
from Tokens import Token, TokenType


class charReader:
    """Class reading character's one by one."""

    # Possible Operations and digits that can be read
    OPERATIONS = '+-*/!^()'
    DIGITS = '0123456789.'

    def __init__(self, exp):
        """Initialize character sequence."""
        self.exp = iter(exp)
        self.generator()

    def generator(self):
        """Provide next character in string."""
        try:
            self.char = next(self.exp)
        except StopIteration:
            self.char = None

    def create_Tokens(self):
        """Check Expression character by character by using a generator."""
        while self.char is not None:
            # If we see a digit, we know it is the beginning of a number
            if self.char in self.DIGITS:
                yield self.generate_Number()

            elif self.char in ' \t\n':  # Any form of whitespace is ignored
                self.generator()
                pass

            # Reading an operation will generate an operation token
            elif self.char in self.OPERATIONS:
                yield self.generate_Operation()

            else:
                raise UnknownElementError(self.char)

    def generate_Number(self):
        """Create the number if the chracters continue representing a digit."""
        num = self.char
        num_decimal_points = 0

        # Code specifically designed for numbers like .1; Python will turn .1 into a float by itself .1 => 0.1
        # As well as the other way around 123. => 123.0
        if num == '.':
            num_decimal_points += 1
            num = '0.'

        self.generator()

        while (self.char is not None and self.char in self.DIGITS):
            if self.char == '.':
                num_decimal_points += 1
                if num_decimal_points > 1:
                    raise ValueError  # Raise a syntax error for numbers with too many decimal points

            num = num + self.char  # The number is built character by character
            self.generator()

        # Return the number TokenType with the float value of it
        return Token(TokenType.NUMBER, float(num))

    def generate_Operation(self):
        """Return the token of the operation."""
        operation = self.char
        self.generator()

        if(operation == '+'):
            return Token(TokenType.PLUS, '+')
        elif(operation == '-'):
            return Token(TokenType.MINUS, '-')
        elif(operation == '*'):
            return Token(TokenType.MULTIPLICATION, '*')
        elif(operation == '/'):
            return Token(TokenType.DIVISION, '/')
        elif(operation == '^'):
            return Token(TokenType.POWER, '^')
        elif(operation == '!'):
            return Token(TokenType.FACTORIAL, '!')
        elif(operation == '('):
            return Token(TokenType.LEFTP, '(')
        elif(operation == ')'):
            return Token(TokenType.RIGHTP, ')')
