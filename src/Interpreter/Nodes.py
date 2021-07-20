"""All possible Nodes for the math expression for the parser to divide in a Tree."""
from dataclasses import dataclass


# The representation functions => __repr__() were used for debugging purposes.
@dataclass
class NumberNode:
    """Represent a Number."""

    value1: float

    def __repr__(self):
        """Represent."""
        return f"{self.value1}"


@dataclass
class AddNode:
    """Representing an Add operation."""

    value1: any
    value2: any

    def __repr__(self):
        """Represent."""
        return f"({self.value1} + {self.value2})"


@dataclass
class MinusNode:
    """Representing an subtract operation."""

    value1: any
    value2: any

    def __repr__(self):
        """Represent."""
        return f"({self.value1} - {self.value2})"


@dataclass
class PositiveNode:
    """For Numbers with a plus in front."""

    Node: any

    def __repr__(self):
        """Represent a number with a Plus in front."""
        return f"(+{self.Node})"


@dataclass
class NegativeNode:
    """For Numbers with a negative in front."""

    Node: any

    def __repr__(self):
        """Represent a negative Number."""
        return f"(-{self.Node})"


@dataclass
class MultiplyNode:
    """Representing a Multiply operation."""

    value1: any
    value2: any

    def __repr__(self):
        """Represent."""
        return f"({self.value1} * {self.value2})"


@dataclass
class DivideNode:
    """Representing a Divide operation."""

    value1: any
    value2: any

    def __repr__(self):
        """Represent."""
        return f"({self.value1} / {self.value2})"


@dataclass
class PowerNode:
    """Representing a Power operation."""

    value1: any
    value2: any

    def __repr__(self):
        """Represent Base^Exponent."""
        return f"({self.value1}^{self.value2})"


@dataclass
class FactorialNode:
    """Representing a Factorial operation."""

    Node: any

    def __repr__(self):
        """Represent a Factorial Number."""
        return f"({self.Node}!)"
