"""Give the answer to the tree."""
from Nodes import AddNode, MinusNode, PositiveNode, NegativeNode, MultiplyNode, DivideNode, PowerNode, FactorialNode, TrigNode, LogNode, SquareRootNode, GammaNode, StandardDeviationNode, MADNode
import math


class EvaluateExpression:
    """Class to provide the answer to the mathematical expression."""

    def __init__(self, tree):
        """Initialize the tree."""
        self.tree = tree

    def getResult(self):
        """Return Result of mathematical Expression through Recursion."""
        # Checks for an operation that requires two terms
        if (isinstance(self.tree, AddNode) or
            isinstance(self.tree, MinusNode) or
            isinstance(self.tree, MultiplyNode) or
            isinstance(self.tree, DivideNode) or
                isinstance(self.tree, PowerNode)):

            # Want to always look at the second number to make sure there isn't a higher precedence function to evaluate first, so we recursively call getResult() on the second term
            mediate_result = EvaluateExpression(self.tree.value2).getResult()

            if isinstance(self.tree, AddNode):  # Evaluate Addition
                mediate_result += EvaluateExpression(self.tree.value1).getResult()

            elif isinstance(self.tree, MinusNode):  # Evaluate Subtraction
                mediate_result = EvaluateExpression(self.tree.value1).getResult() - mediate_result

            elif isinstance(self.tree, MultiplyNode):  # Evaluate Multiplication
                mediate_result *= EvaluateExpression(self.tree.value1).getResult()

            elif isinstance(self.tree, DivideNode):  # Evaluate Division
                mediate_result = EvaluateExpression(self.tree.value1).getResult() / mediate_result

            elif isinstance(self.tree, PowerNode):  # Evaluate Power
                mediate_result = EvaluateExpression(self.tree.value1).getResult()**mediate_result  # ---------------------

        # Checks for the operation that requires just a single number
        # Evaluates a negative number
        elif isinstance(self.tree, NegativeNode):
            mediate_result = -1 * EvaluateExpression(self.tree.Node).getResult()

        # Evaluates a positive number
        elif isinstance(self.tree, PositiveNode):
            mediate_result = EvaluateExpression(self.tree.Node).getResult()

        # Factorial Function
        elif isinstance(self.tree, FactorialNode):
            mediate_result = math.factorial(EvaluateExpression(self.tree.Node).getResult())  # -------------------

        elif isinstance(self.tree, SquareRootNode):
            mediate_result = EvaluateExpression(self.tree.Node).getResult()**0.5

        # Evaluates a Trigonometry function, inverse trigonometric function or hyperbolic trigonometry funciton
        elif isinstance(self.tree, TrigNode):
            if self.tree.function == 'sin':
                mediate_result = math.sin(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'cos':
                mediate_result = math.cos(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'tan':
                mediate_result = math.tan(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'arcsin':
                mediate_result = math.asin(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'arccos':
                mediate_result = math.acos(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'arctan':
                mediate_result = math.atan(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'sinh':  #
                mediate_result = math.sinh(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'cosh':  #
                mediate_result = math.cosh(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'tanh':  #
                mediate_result = math.tanh(EvaluateExpression(self.tree.Node).getResult())

        elif isinstance(self.tree, LogNode):  #
            mediate_result = math.log(EvaluateExpression(self.tree.value2).getResult(), EvaluateExpression(self.tree.value1).getResult())

        elif isinstance(self.tree, GammaNode):  #
            mediate_result = EvaluateExpression(self.tree.Node).getResult()*2

        elif isinstance(self.tree, StandardDeviationNode):
            mediate_result = EvaluateExpression(self.computeList(self.tree.Node))

        elif isinstance(self.tree, MADNode):
            mediate_result = 0

        else:
            # When the second term in an expression is calculated, we can now perform the operation with the first term
            mediate_result = self.tree.value1

        # Returns the intermediary result in the mathematical expression
        return mediate_result

    def computeList(self, list):
        """For Standard Deviation and MAD in the expressions."""
        newlist = []
        for i in list:
            result = EvaluateExpression(i).getResult()
            print('HI ' + str(result))
            newlist.append(result)

        return newlist
