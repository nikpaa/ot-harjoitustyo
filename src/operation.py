class Operation:
    def __init__(self, type_of_operation: str):
        if not type_of_operation in ["+", "-", "/", "*"]:
            raise ValueError(f"Operation '{type_of_operation}' is unsupported")
        self.__type_of_operation = type_of_operation

    def compute(self, num1: float, num2: float) -> float:
        if self.__type_of_operation == "+":
            return num1 + num2
        elif self.__type_of_operation == "-":
            return num1 - num2
        elif self.__type_of_operation == "/":
            if num2 == 0:
                raise ZeroDivisionError
            return num1 / num2
        elif self.__type_of_operation == "*":
            return num1*num2
        else:
            raise ValueError(f"Operation '{self.__type_of_operation}' is unsupported")

    def __str__(self):
        return self.__type_of_operation