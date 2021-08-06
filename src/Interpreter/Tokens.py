"""Classes of all possible types that can appear in a mathematical expression."""
from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    """Enumeration of all possible Token Types."""

    "Since they are constant, and this is an easy way to allow us to know which ones we are manipulating."

    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLICATION = 3
    DIVISION = 4
    POWER = 5
    FACTORIAL = 6
    TRIG = 7
    LOGARITHMIC = 8
    STANDARDDEVIATION = 9
    GAMMA = 10
    MAD = 11
    PI = 12
    E = 13
    SQUAREROOT = 14
    LEFTP = 15
    RIGHTP = 16
    LEFTB = 17
    RIGHTB = 18
    COMMA = 19


@dataclass
class Token:
    """Stores the Type of Token and it value if any."""

    type: TokenType
    value: any = None

    def __repr__(self):
        """Output the Token (Debugging Purposes)."""
        return self.type.name + str({f'{self.value}' if self.value is not None else ''})
