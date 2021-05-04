from operation import BinaryOperation, UnaryOperation
import history

def parse_input(input_str: str) -> (bool, str):

    """ Parses user input and calls relevant functions based on the input.

    """

    if input_str.lower() == "help":
        print("Commands:\n")
        print("'operations' lists the supported operations")
        print("'history'    prints previously executed calculations")
        print("'exit'       exits the program")
        print("")
        return (True, None)

    if input_str.lower() == "operations":
        print("Supported operations are:")
        operations = BinaryOperation("+").get_supported_operations() + UnaryOperation("exp").get_supported_operations()
        for op in operations:
            print(op)
        return (True, None)

    if input_str.lower() == "history":
        history.print_history()
        return (True, None)

    elif input_str.lower() == "exit":
        return (False, None)

    else:
        return (True, str(parse_expression(input_str)))


def parse_expression(expression: str) -> float:
    (first_num, rest) = parse_num(expression)
    return parse_expression_rec(first_num, rest)


def parse_expression_rec(first_num: float, expression: str) -> float:
    """ Parses the expression recursively

        Returns
            to itself recursively until parsing is done

    """

    if len(expression) == 0:
        return first_num

    # try parsing a number, if it fails parse a unary operation
    try:
        (second_num, rest) = parse_num(expression)
        (operation, rest) = parse_bin_op(rest)
        result = operation.compute(first_num, second_num)
    except ValueError:
        (operation, rest) = parse_un_op(expression)
        result = operation.compute(first_num)

    return parse_expression_rec(result, rest)



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


def parse_un_op(expression: str) -> (UnaryOperation, str):
    (op_as_string, rest) = parse_token(expression)

    return (UnaryOperation(op_as_string), rest)

def parse_bin_op(expression: str) -> (BinaryOperation, str):
    (op_as_string, rest) = parse_token(expression)

    return (BinaryOperation(op_as_string), rest)
