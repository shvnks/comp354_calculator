"""Raising Error when an unknown element/character is revealed in the math expression."""


class UnknownElementError(Exception):
    """Unknown character Error."""

    def __init__(self, message) -> None:
        """Initialize Error."""
        super().__init__(message)


class NoExpression(Exception):
    """No expression is mentioned."""

    pass


class TooManyDecimalsException(Exception):
    """Too many deciamls in a number."""

    def __init__(self, message) -> None:
        """Initialize Error."""
        super().__init__(message)


class MissingParenthesisException(Exception):
    """Parentheses not coming in pairs."""

    def __init__(self, message) -> None:
        """Initialize Error."""
        super().__init__(message)


class SyntaxException(Exception):
    """Syntax Error."""

    def __init__(self, message) -> None:
        """Initialize Error."""
        super().__init__(message)
