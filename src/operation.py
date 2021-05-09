import math
from errors import CalculatorError

class Operation:
    """ Class for handling operations

    Contains unary and binary operations as subclasses.
    """
    def get_supported_operations(self) -> list:
        """ Returns a list of supported operations
        """
        return self.supported_operations


class UnaryOperation(Operation):
    """ Subclass for handling unary operations.
    """

    def __init__(self, type_of_operation: str):
        """ Initialize the class with the type of the operation
        """
        self.supported_operations = ["exp", "ln"]
        if not type_of_operation in self.supported_operations:
            raise CalculatorError(f"Operation '{type_of_operation}' is unsupported")
        self.__type_of_operation = type_of_operation

    def compute(self, num1: float) -> float:
        """ Compure a value given the unary operation and its input
        """
        if self.__type_of_operation == "exp":
            return math.exp(num1)
        if self.__type_of_operation == "ln":
            if num1 > 0:
                return math.log(num1)
            raise CalculatorError("Logarithm of non-positive number")

        raise CalculatorError(f"Operation '{self.__type_of_operation}' is unsupported")

    def __str__(self) -> str:
        """ Return a list of supported unary operations
        """
        return self.__type_of_operation


class BinaryOperation(Operation):
    """ Subclass for handling unary operations.
    """
    def __init__(self, type_of_operation: str):
        self.supported_operations = ["+", "-", "/", "*"]
        if not type_of_operation in self.supported_operations:
            raise CalculatorError(f"Operation '{type_of_operation}' is unsupported")
        self.__type_of_operation = type_of_operation

    def compute(self, num1: float, num2: float) -> float:
        """ Compure a value given the binary operation and its inputs
        """

        if self.__type_of_operation == "+":
            return num1 + num2
        if self.__type_of_operation == "-":
            return num1 - num2
        if self.__type_of_operation == "/":
            if num2 == 0:
                raise CalculatorError("Division by zero")
            return num1 / num2
        if self.__type_of_operation == "*":
            return num1*num2

        raise CalculatorError(f"Operation '{self.__type_of_operation}' is unsupported")

    def __str__(self) -> str:
        """ Return a list of supported binary operations
        """
        return self.__type_of_operation
