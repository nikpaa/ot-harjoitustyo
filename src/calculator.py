import history
from parse import parse_expression


print("Calculator launched.")
history.create_table()
history.clear_table()

while True:
    try:
        operation = input("")
        result = parse_expression(operation)
        history.add_operation_to_db(operation, result)
        print(result)
        question = input("Do you want to print history (y, n)?")
        if question == "y":
            history.print_history()
    except Exception as e:
        print(e)
        question = input("Do you want to print history (y, n)?")
        if question == "y":
            history.print_history()
    
    