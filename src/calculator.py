from parse import parse_expression

print("Calculator launched.")

while True:

    laskutoimitus = input("")

    print(parse_expression(laskutoimitus))