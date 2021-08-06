"""Give the answer to the tree."""
from Nodes import AddNode, MinusNode, PositiveNode, NegativeNode, MultiplyNode, DivideNode, PowerNode, FactorialNode, TrigNode, LogNode, SquareRootNode, GammaNode, StandardDeviationNode, MADNode
import math
import sys
sys.path.insert(0, 'C:\\Users\\Nicholas\\Desktop\\COMP354\\comp354_calculator\\src')
from FunctionStandardDeviation import FunctionStandardDeviation
from FunctionGamma import FunctionGamma
from FunctionMAD import FunctionMAD
from FunctionLog import FunctionLog
from FunctionArccos import FunctionArccos
from FunctionArcsin import FunctionArcsin
from FunctionSinh import FunctionSinh
from FunctionTanh import FunctionTanh
from FunctionCosh import FunctionCosh
from FunctionExponent import FunctionExponent
from FunctionFactorial import FunctionFactorial


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
                mediate_result = FunctionExponent(EvaluateExpression(self.tree.value1).getResult(), mediate_result).calculateEquation()

        # Checks for the operation that requires just a single number
        # Evaluates a negative number
        elif isinstance(self.tree, NegativeNode):
            mediate_result = -1 * EvaluateExpression(self.tree.Node).getResult()

        # Evaluates a positive number
        elif isinstance(self.tree, PositiveNode):
            mediate_result = EvaluateExpression(self.tree.Node).getResult()

        # Factorial Function
        elif isinstance(self.tree, FactorialNode):
            mediate_result = FunctionFactorial(EvaluateExpression(self.tree.Node).getResult()).calculateEquation()

        elif isinstance(self.tree, SquareRootNode):
            mediate_result = FunctionExponent(EvaluateExpression(self.tree.Node).getResult(), 0.5).calculateEquation()

        # Evaluates a Trigonometry function, inverse trigonometric function or hyperbolic trigonometry funciton
        elif isinstance(self.tree, TrigNode):
            if self.tree.function == 'sin':
                mediate_result = math.sin(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'cos':
                mediate_result = math.cos(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'tan':
                mediate_result = math.tan(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'arcsin':
                mediate_result = FunctionArcsin(EvaluateExpression(self.tree.Node).getResult()).calculateEquation()
            if self.tree.function == 'arccos':
                mediate_result = FunctionArccos(EvaluateExpression(self.tree.Node).getResult()).calculateEquation()
            if self.tree.function == 'arctan':
                mediate_result = math.atan(EvaluateExpression(self.tree.Node).getResult())
            if self.tree.function == 'sinh':  #
                mediate_result = FunctionSinh(EvaluateExpression(self.tree.Node).getResult()).calculateEquation()
            if self.tree.function == 'cosh':  #
                mediate_result = FunctionCosh(EvaluateExpression(self.tree.Node).getResult()).calculateEquation()
            if self.tree.function == 'tanh':  #
                mediate_result = FunctionTanh(EvaluateExpression(self.tree.Node).getResult()).calculateEquation()

        elif isinstance(self.tree, LogNode):
            mediate_result = FunctionLog(EvaluateExpression(self.tree.value2).getResult(), EvaluateExpression(self.tree.value1).getResult()).calculateEquation()

        elif isinstance(self.tree, GammaNode):
            mediate_result = FunctionGamma(EvaluateExpression(self.tree.Node).getResult()).calculateEquation()

        elif isinstance(self.tree, StandardDeviationNode):
            mediate_result = FunctionStandardDeviation(self.computeList(self.tree.Node)).standardDeviation()

        elif isinstance(self.tree, MADNode):
            mediate_result = FunctionMAD(self.computeList(self.tree.Node)).calculateEquation()

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
            newlist.append(result)

        return newlist
