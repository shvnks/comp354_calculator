"""Reads math expression one character at a time."""
from InterpreterErrors import UnknownElementError, TooManyDecimalsException, SyntaxException
from Tokens import Token, TokenType


class charReader:
    """Class reading character's one by one."""

    # Possible Operations and digits that can be read
    OPERATIONS = '+-*/!^()\u221a[]'
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

    def createTokens(self):
        """Check Expression character by character by using a generator."""
        while self.char is not None:
            # If we see a digit, we know it is the beginning of a number
            if self.char in self.DIGITS:
                yield self.generateNumber()

            elif self.char in ' \t\n,':  # Any form of whitespace is ignored
                self.generator()
                pass

            # Reading an operation will generate an operation token
            elif self.char in self.OPERATIONS:
                yield self.generateOperation()

            # Reading letters for the beginning of a trig, or special function (MAD, Gamma, σ)
            elif self.char in 'ascltMσΓ':
                yield self.generateFunction()

<<<<<<< HEAD
            elif self.char in '\u03c0':
=======
            elif self.char in '\U0001D745':
>>>>>>> 7934e8bd1ca63632e704871a9ba8f074ad79e04a
                self.generator()
                yield Token(TokenType.PI, float(3.1415926535897932384626433))

            elif self.char in 'e':
                self.generator()
                yield Token(TokenType.E, float(2.7182818284590452353602874))

            else:
                raise UnknownElementError(f'UNKNOWN SYMBOL ERROR: {self.char}')

    def generateFunction(self):
        """Create the token for a special function."""
        functionName = self.char
        self.generator()

        while self.char is not None and functionName not in ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'log', 'MAD', 'σ', 'Γ']:
            functionName = functionName + self.char
            self.generator()

        if self.char == 'h' and functionName in ['sin', 'cos', 'tan']:
            functionName = functionName + self.char
            self.generator()

        if functionName == 'log':
            return Token(TokenType.LOGARITHMIC, functionName)
        elif functionName == 'MAD':
            return Token(TokenType.MAD, 'MAD')
        elif functionName == 'Γ':
            return Token(TokenType.GAMMA, 'Γ')
        elif functionName == 'σ':
            return Token(TokenType.STANDARDDEVIATION, 'σ')

        return Token(TokenType.TRIG, functionName)

    def generateNumber(self):
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
                    raise TooManyDecimalsException('SYNTAX ERROR: Too many decimals')  # Raise a syntax error for numbers with too many decimal points

            num = num + self.char  # The number is built character by character
            self.generator()

        # Return the number TokenType with the float value of it
        return Token(TokenType.NUMBER, float(num))

    def generateOperation(self):
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
        elif(operation == '\u221a'):
            return Token(TokenType.SQUAREROOT, '\u221a')
        elif(operation == '^'):
            return Token(TokenType.POWER, '^')
        elif(operation == '!'):
            return Token(TokenType.FACTORIAL, '!')
        elif(operation == '('):
            return Token(TokenType.LEFTP, '(')
        elif(operation == ')'):
            return Token(TokenType.RIGHTP, ')')
        elif(operation == '['):
            return Token(TokenType.LEFTB, '[')
        elif(operation == ']'):
            return Token(TokenType.RIGHTB, ']')
