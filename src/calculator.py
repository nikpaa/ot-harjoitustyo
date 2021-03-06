from history import add_operation_to_db, create_table, clear_table
from parse import parse_input
from errors import CalculatorError

print("Calculator launched. Type 'help' for a list of commands.")
create_table()

while True:
    try:
        operation = input("> ")
        (advance, result) = parse_input(operation)
        if not advance:
            break

        if result is not None:
            add_operation_to_db(operation, result)
            print(result)

    except (CalculatorError, ValueError) as err:
        print(err)
        print("Type 'help' for a list of commands.")

save_question = input("Save history? (y/n) ")
if save_question != "y":
    clear_table()
