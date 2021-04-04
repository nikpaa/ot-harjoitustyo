
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



def parse_expression(expression: str) -> float:
    (first_num, rest) = parse_num(expression)
    (second_num, rest) = parse_num(rest)
    (operation, rest) = parse_op(rest)
    return operation.compute(first_num, second_num)

def parse_token(expression: str) -> (str, str):

    current_ind = 0
    current_string = ""
    while current_ind < len(expression) and expression[current_ind] != " ":
        current_string += expression[current_ind]
        current_ind += 1

    return (current_string, expression[current_ind+1:])

def parse_num(expression: str) -> (float, str):

    (num_as_string, rest) = parse_token(expression)
    
    return (float(num_as_string), rest)

def parse_op(expression: str) -> (Operation, str):

    (op_as_string, rest) = parse_token(expression)
    
    return (Operation(op_as_string), rest)


print("Calculator launched.")

while True:

    laskutoimitus = input("")

    print(parse_expression(laskutoimitus))