from errors import CalculatorError
import math

class Operation:
    def get_supported_operations(self) -> list:
        return self.supported_operations

    def __str__(self) -> str:
        return self.__type_of_operation


class UnaryOperation(Operation):
    def __init__(self, type_of_operation: str):
        self.supported_operations = ["exp", "ln"]
        if not type_of_operation in self.supported_operations:
            raise CalculatorError(f"Operation '{type_of_operation}' is unsupported")
        self.__type_of_operation = type_of_operation

    def compute(self, num1: float) -> float:
        if self.__type_of_operation == "exp":
            return math.exp(num1)
        if self.__type_of_operation == "ln":
            if num1 > 0:
                return math.log(num1)
            raise CalculatorError(f"Logarithm of non-positive number")

        raise CalculatorError(f"Operation '{self.__type_of_operation}' is unsupported")


class BinaryOperation(Operation):
    def __init__(self, type_of_operation: str):
        self.supported_operations = ["+", "-", "/", "*"]
        if not type_of_operation in self.supported_operations:
            raise CalculatorError(f"Operation '{type_of_operation}' is unsupported")
        self.__type_of_operation = type_of_operation

    def compute(self, num1: float, num2: float) -> float:
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
