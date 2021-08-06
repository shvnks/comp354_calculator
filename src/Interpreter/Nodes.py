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


@dataclass
class TrigNode:
    """Representing a Trigonometry, inverse trigonometric or hyperbolic operation."""

    Node: any
    function: str

    def __repr__(self):
        """Represent a Trig value."""
        return f"({self.function}({self.Node}))"


@dataclass
class LogNode:
    """Representing a Trigonometry, inverse trigonometric or hyperbolic operation."""

    value1: any
    value2: any

    def __repr__(self):
        """Represent a Trig value."""
        return f"(log{self.value1}({self.value2}))"


@dataclass
class SquareRootNode:
    """Representing a square root operation."""

    Node: any

    def __repr__(self):
        """Represent a square root Number."""
        return f"(√{self.Node})"


@dataclass
class MADNode:
    """Representing a MAD operation."""

    Node: any

    def __repr__(self):
        """Represent a Median Absolute Deviation Calculation."""
        return f"(MAD{self.Node})"


@dataclass
class GammaNode:
    """Representing a Gamma (Γ) operation."""

    Node: any

    def __repr__(self):
        """Represent a Gamma calculation."""
        return f"Γ({self.Node})"


@dataclass
class StandardDeviationNode:
    """Representing a standard deviation (σ) operation."""

    Node: any

    def __repr__(self):
        """Represent a Standard Deviation Calculation."""
        return f"σ({self.Node})"
