"""Take individual tokens, and make the math expression."""
from Tokens import TokenType
from Nodes import NumberNode, AddNode, MinusNode, PositiveNode, NegativeNode, MultiplyNode, DivideNode, PowerNode, FactorialNode
from InterpreterErrors import NoExpression


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

    def read_Tokens(self):
        """Check Entire Expression."""
        if self.current_token is None:
            raise NoExpression

        # Beginning of Journey to the answer
        result = self.evaluate_low_precedence()

        # Any other token the interpreter missed will raise a Syntax Error. This code mostly raised with missing parenthesis
        if self.current_token is not None:
            raise ValueError

        return result

    def evaluate_low_precedence(self):
        """Acquire Lowest precedence operations (Addition == Subtraction)."""
        mediate_result = self.evaluate_higher_precedence()

        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.generator()
                mediate_result = AddNode(mediate_result, self.evaluate_higher_precedence())
            elif self.current_token.type == TokenType.MINUS:
                self.generator()
                mediate_result = MinusNode(mediate_result, self.evaluate_higher_precedence())

        return mediate_result

    def evaluate_higher_precedence(self):
        """Acquire Higher Precedence Values (Multiplication == Division)."""
        mediate_result = self.evaluate_highest_precedence()

        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLICATION, TokenType.DIVISION):
            if self.current_token.type == TokenType.MULTIPLICATION:
                self.generator()
                mediate_result = MultiplyNode(mediate_result, self.evaluate_highest_precedence())
            elif self.current_token.type == TokenType.DIVISION:
                self.generator()
                mediate_result = DivideNode(mediate_result, self.evaluate_highest_precedence())

        return mediate_result

    def evaluate_highest_precedence(self):
        """Acquire Precedence of upmost importance (Factorail > Power)."""
        mediate_result = self.Acquire_Number()

        while self.current_token is not None and self.current_token.type is TokenType.FACTORIAL:
            self.generator()
            mediate_result = FactorialNode(mediate_result)

        while self.current_token is not None and self.current_token.type is TokenType.POWER:
            self.generator()
            mediate_result = PowerNode(mediate_result, self.evaluate_highest_precedence())

        return mediate_result

    def Acquire_Number(self):
        """Look for Numbers between operators."""
        token = self.current_token  # Keep track of "previous" token, which acts as the first term in an operation

        # If the expression reads a token that is just an operator with no Number
        if self.current_token is None:
            raise ValueError

        self.generator()  # Move to the next token in the expression

        if token.type is TokenType.LEFTP:  # Treat a left parenthesis as the beginning of a new expression
            result = self.evaluate_low_precedence()

            # Checks for a coresponding right parenthesis to close the new expression
            if self.current_token is None or self.current_token.type != TokenType.RIGHTP:
                raise ValueError

            self.generator()  # Move past the right parenthesis

            # Treat parenthesis as hidden multiplication ()() and ()#
            if (self.current_token is not None and self.current_token.type is TokenType.LEFTP) or (self.current_token is not None and self.current_token.type is TokenType.NUMBER):
                result = MultiplyNode(result, self.Acquire_Number())

            # Return result from the expression after the left parenthesis
            return result

        elif token.type == TokenType.NUMBER:

            # Code to consider #() as a multiplication
            if self.current_token is not None and self.current_token.type is TokenType.LEFTP:
                return MultiplyNode(NumberNode(token.value), self.Acquire_Number())

            return NumberNode(token.value)

        # Case where user inputs a number like +#
        elif token.type is TokenType.PLUS:
            return PositiveNode(self.Acquire_Number())

        # Case where user inputs a number like -#
        elif token.type is TokenType.MINUS:
            return NegativeNode(self.Acquire_Number())

        # Special factorial case, since the number appears before the operator
        elif self.current_token is not None and token.type is TokenType.FACTORIAL:
            return FactorialNode(token.value)

        # Any other Syntax Errors will be caught by this raise Exception
        raise ValueError
