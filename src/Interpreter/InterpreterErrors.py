"""Raising Error when an unknown element/character is revealed in the math expression."""
from dataclasses import dataclass


@dataclass
class UnknownElementError(Exception):
    """Unknown character Error."""

    element: str
    pass


class NoExpression(Exception):
    """No expression is mentioned."""

    pass
