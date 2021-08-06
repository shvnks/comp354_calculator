"""Give the answer to the tree."""
import math

from Nodes import *

import FunctionFactorial
import FunctionExponent
import FunctionGamma
import FunctionLog
import FunctionSinh
import FunctionCosh
import FunctionTanh
import FunctionArccos
import FunctionArcsin
import FunctionArctan
import FunctionStandardDeviation
import FunctionGamma
import FunctionMAD


class EvaluateExpression:
    """Class to provide the answer to the mathematical expression."""

    def __init__(self, tree):
        """Initialize the tree."""
        self.tree = tree

    def getResult(self, isDeg : bool = False):
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
                mediate_result = FunctionExponent.FunctionExponent(EvaluateExpression(self.tree.value1).getResult(), mediate_result).calculateEquation()

        # Checks for the operation that requires just a single number
        # Evaluates a negative number
        elif isinstance(self.tree, NegativeNode):
            mediate_result = -1 * EvaluateExpression(self.tree.Node).getResult()

        # Evaluates a positive number
        elif isinstance(self.tree, PositiveNode):
            mediate_result = EvaluateExpression(self.tree.Node).getResult()

        # Factorial Function
        elif isinstance(self.tree, FactorialNode):
            mediate_result = FunctionFactorial.FunctionFactorial(EvaluateExpression(self.tree.Node).getResult()).calculateEquation()

        elif isinstance(self.tree, SquareRootNode):
            mediate_result = FunctionExponent.FunctionExponent(EvaluateExpression(self.tree.Node).getResult(), 0.5).calculateEquation()

        # Evaluates a Trigonometry function, inverse trigonometric function or hyperbolic trigonometry funciton
        elif isinstance(self.tree, TrigNode):
            if self.tree.function == 'sin':
                result = EvaluateExpression(self.tree.Node).getResult()
                if isDeg:
                    result = math.radians(result)
                mediate_result = math.sin(result)
            if self.tree.function == 'cos':
                result = EvaluateExpression(self.tree.Node).getResult()
                if isDeg:
                    result = math.radians(result)
                mediate_result = math.cos(result)
            if self.tree.function == 'tan':
                result = EvaluateExpression(self.tree.Node).getResult()
                if isDeg:
                    result = math.radians(result)
                mediate_result = math.tan(result)
            if self.tree.function == 'arcsin':
                mediate_result = FunctionArcsin.FunctionArcsin(EvaluateExpression(self.tree.Node).getResult()).calculateEquation(isDeg)
            if self.tree.function == 'arccos':
                mediate_result = FunctionArccos.FunctionArccos(EvaluateExpression(self.tree.Node).getResult()).calculateEquation(isDeg)
            if self.tree.function == 'arctan':
                mediate_result = FunctionArctan.FunctionArctan(EvaluateExpression(self.tree.Node).getResult()).calculateEquation(isDeg)
            if self.tree.function == 'sinh':  #
                mediate_result = FunctionSinh.FunctionSinh(EvaluateExpression(self.tree.Node).getResult()).calculateEquation(isDeg)
            if self.tree.function == 'cosh':  #
                mediate_result = FunctionCosh.FunctionCosh(EvaluateExpression(self.tree.Node).getResult()).calculateEquation(isDeg)
            if self.tree.function == 'tanh':  #
                mediate_result = FunctionTanh.FunctionTanh(EvaluateExpression(self.tree.Node).getResult()).calculateEquation(isDeg)

        elif isinstance(self.tree, LogNode):  #
            mediate_result = FunctionLog.FunctionLog(EvaluateExpression(self.tree.value1).getResult(), EvaluateExpression(self.tree.value2).getResult()).calculateEquation()

        elif isinstance(self.tree, GammaNode):  #
            mediate_result = FunctionGamma.FunctionGamma(EvaluateExpression(self.tree.Node).getResult()).calculateEquation()

        elif isinstance(self.tree, StandardDeviationNode):
            mediate_result = FunctionStandardDeviation.FunctionStandardDeviation(self.computeList(self.tree.Node)).calculateEquation()

        elif isinstance(self.tree, MADNode):
            mediate_result = FunctionMAD.FunctionMAD(self.computeList(self.tree.Node)).calculateEquation()

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
