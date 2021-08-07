"""Take individual tokens, and make the math expression."""
from Tokens import TokenType
from Nodes import *
from InterpreterErrors import NoExpression, MissingParenthesisException, SyntaxException

class CreateExpression:
    """Create Expression => knowing what the expression is asking."""

    def __init__(self, tokens):
        """Initialize the set of tokens as an iterator (generator)."""
        self.tokens = iter(tokens)
        self.generator()

    def generator(self):
        """Use Generator to advance through the list of tokens."""
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def readTokens(self):
        """Check Entire Expression."""
        if self.current_token is None:
            raise NoExpression

        # Beginning of Journey to the answer
        result = self.evaluateLowPrecedence()

        # Any other token the interpreter missed will raise a Syntax Error. This code mostly raised with missing parenthesis
        if self.current_token is not None:
            raise MissingParenthesisException('SYNTAX ERROR: Missing Parenthesis')

        return result

    def evaluateLowPrecedence(self):
        """Acquire Lowest precedence operations (Addition == Subtraction)."""
        mediate_result = self.evaluateHigherPrecedence()

        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.generator()
                mediate_result = AddNode(mediate_result, self.evaluateHigherPrecedence())
            elif self.current_token.type == TokenType.MINUS:
                self.generator()
                mediate_result = MinusNode(mediate_result, self.evaluateHigherPrecedence())

        return mediate_result

    def evaluateHigherPrecedence(self):
        """Acquire Higher Precedence Values (Multiplication == Division)."""
        mediate_result = self.evaluateHighestPrecedence()

        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLICATION, TokenType.NUMBER, TokenType.LEFTP, TokenType.DIVISION, TokenType.TRIG, TokenType.LOGARITHMIC, TokenType.SQUAREROOT, TokenType.GAMMA, TokenType.STANDARDDEVIATION, TokenType.MAD):
            if self.current_token.type == TokenType.MULTIPLICATION:
                self.generator()
                mediate_result = MultiplyNode(mediate_result, self.evaluateHighestPrecedence(True))
            elif self.current_token.type is TokenType.LEFTP or self.current_token.type is TokenType.NUMBER:
                mediate_result = MultiplyNode(mediate_result, self.evaluateHighestPrecedence(True))
            elif self.current_token.type == TokenType.DIVISION:
                self.generator()
                mediate_result = DivideNode(mediate_result, self.evaluateHighestPrecedence(True))
            elif self.current_token.type is TokenType.TRIG:
                # For very specific syntax like cos0cos1
                mediate_result = MultiplyNode(mediate_result, self.acquireNumber())
            elif self.current_token.type is TokenType.LOGARITHMIC:
                mediate_result = MultiplyNode(mediate_result, self.acquireNumber())
            elif self.current_token.type is TokenType.SQUAREROOT:
                mediate_result = MultiplyNode(mediate_result, self.acquireNumber())
            elif self.current_token.type is TokenType.GAMMA:
                mediate_result = MultiplyNode(mediate_result, self.acquireNumber())
            elif self.current_token.type is TokenType.STANDARDDEVIATION:
                mediate_result = MultiplyNode(mediate_result, self.acquireNumber())
            elif self.current_token.type is TokenType.MAD:
                mediate_result = MultiplyNode(mediate_result, self.acquireNumber())

        return mediate_result

    def evaluateHighestPrecedence(self, needTwoValues=False):
        """Acquire Precedence of upmost importance (Factorial > Power)."""
        mediate_result = self.acquireNumber(needTwoValues)

        while self.current_token is not None and self.current_token.type is TokenType.FACTORIAL:
            self.generator()
            mediate_result = FactorialNode(mediate_result)

        while self.current_token is not None and self.current_token.type is TokenType.POWER:
            self.generator()
            mediate_result = PowerNode(mediate_result, self.evaluateHighestPrecedence(True))

        return mediate_result

    def acquireNumber(self, needTwoValues=False):
        """Look for Numbers between operators."""
        token = self.current_token  # Keep track of "previous" token, which acts as the first term in an operation

        # If the expression reads a token that is just an operator with no Number
        if self.current_token is None:
            raise SyntaxException('SYNTAX ERROR')

        self.generator()  # Move to the next token in the expression

        if token.type is TokenType.LEFTP:  # Treat a left parenthesis as the beginning of a new expression
            result = self.evaluateLowPrecedence()

            # Checks for a coresponding right parenthesis to close the new expression
            if self.current_token is None or self.current_token.type != TokenType.RIGHTP:
                raise MissingParenthesisException('SYNTAX ERROR: Missing Parenthesis')

            self.generator()  # Move past the right parenthesis

            if needTwoValues is True:  # Checks for multiple parenthesis in a row for function like log, trig and √
                return result

            # Treat parenthesis as hidden multiplication ()() and ()#
            if ((self.current_token is not None and self.current_token.type is TokenType.LEFTP)
                or (self.current_token is not None and self.current_token.type is TokenType.NUMBER)
                    or (self.current_token is not None and self.current_token.type is TokenType.PI)
                    or (self.current_token is not None and self.current_token.type is TokenType.E)):
                result = MultiplyNode(result, self.acquireNumber())

            # Return result from the expression after the left parenthesis
            return result

        elif token.type == TokenType.NUMBER or token.type == TokenType.PI or token.type == TokenType.E:

            # Code to consider #() as a multiplication, as well as #e#, ##
            if self.current_token is not None and (self.current_token.type is TokenType.LEFTP or
               self.current_token.type is TokenType.PI or self.current_token.type is TokenType.NUMBER or
               self.current_token.type is TokenType.E) and needTwoValues is False:
                return MultiplyNode(NumberNode(token.value), self.acquireNumber())

            return NumberNode(token.value)

        elif token.type == TokenType.LEFTB:
            list = []
            while self.current_token.type is not None and self.current_token.type is not TokenType.RIGHTB:
                argument = self.acquireNumber(True)
                list.append(argument)

            self.generator()  # Get past ]
            return list

        # Case where user inputs a number like +#
        elif token.type is TokenType.PLUS:
            return PositiveNode(self.evaluateHighestPrecedence())

        # Case where user inputs a number like -#
        elif token.type is TokenType.MINUS:
            return NegativeNode(self.evaluateHighestPrecedence())

        # Case with square root symbol √
        elif token.type is TokenType.SQUAREROOT:
            return SquareRootNode(self.evaluateHighestPrecedence(True))

        # Case of finding a trig function
        elif token.type is TokenType.TRIG:
            return TrigNode(self.evaluateHighestPrecedence(True), token.value)  # token.value is the function, so sin sinh cosh arctan etc...

        # Case of logarithm(a)(b)
        elif token.type is TokenType.LOGARITHMIC:
            return LogNode(self.acquireNumber(True), self.acquireNumber(True))

        elif token.type is TokenType.MAD:
            return MADNode(self.acquireNumber())

        elif token.type is TokenType.GAMMA:
            return GammaNode(self.evaluateHighestPrecedence(True))

        # Case for standard deviation
        elif token.type is TokenType.STANDARDDEVIATION:
            return StandardDeviationNode(self.acquireNumber())

        # Special factorial case, since the number appears before the operator
        elif self.current_token is not None and token.type is TokenType.FACTORIAL:
            return FactorialNode(token.value)

        # Any other Syntax Errors will be caught by this raise Exception
        raise SyntaxException('SYNTAX ERROR')
