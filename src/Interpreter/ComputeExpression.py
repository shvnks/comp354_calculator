"""Give the answer to the tree."""
from Nodes import AddNode, MinusNode, PositiveNode, NegativeNode, MultiplyNode, DivideNode, PowerNode, FactorialNode
import math


class EvaluateExpression:
    """Class to provide the answer to the mathematical expression."""

    def __init__(self, tree):
        """Initialize the tree."""
        self.tree = tree

    def get_Result(self):
        """Return Result of mathematical Expression through Recursion."""
        # Checks for an operation that requires two terms
        if isinstance(self.tree, AddNode) or isinstance(self.tree, MinusNode) or isinstance(self.tree, MultiplyNode) or isinstance(self.tree, DivideNode) or isinstance(self.tree, PowerNode):

            # Want to always look at the second number to make sure there isn't a higher precedence fucntion to evaluate first, so we recursively call get_Result() on the second term
            mediate_result = EvaluateExpression(self.tree.value2).get_Result()

            if isinstance(self.tree, AddNode):  # Evaluate Addition
                mediate_result += EvaluateExpression(self.tree.value1).get_Result()

            elif isinstance(self.tree, MinusNode):  # Evaluate Subtraction
                mediate_result = EvaluateExpression(self.tree.value1).get_Result() - mediate_result

            elif isinstance(self.tree, MultiplyNode):  # Evaluate Multiplication
                mediate_result *= EvaluateExpression(self.tree.value1).get_Result()

            elif isinstance(self.tree, DivideNode):  # Evaluate Division
                mediate_result = EvaluateExpression(self.tree.value1).get_Result() / mediate_result

            elif isinstance(self.tree, PowerNode):  # Evaluate Power
                mediate_result = EvaluateExpression(self.tree.value1).get_Result()**mediate_result  # ---------------------

        # Checks for the operation that requires just a single number
        # Evaluates a negative number
        elif isinstance(self.tree, NegativeNode):
            mediate_result = -1 * EvaluateExpression(self.tree.Node).get_Result()

        # Evaluates a positive number
        elif isinstance(self.tree, PositiveNode):
            mediate_result = EvaluateExpression(self.tree.Node).get_Result()

        elif isinstance(self.tree, FactorialNode):  # Factorial Function
            mediate_result = math.factorial(EvaluateExpression(self.tree.Node).get_Result())  # -------------------

        else:
            # When the second term in an expression is calculated, we can now perform the operation with the first term
            mediate_result = self.tree.value1

        # Returns the intermediary result in the mathematical expression
        return mediate_result
