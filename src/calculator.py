from parse import parse_expression

print("Calculator launched.")

while True:
    try:
        laskutoimitus = input("")
        print(parse_expression(laskutoimitus))
    except Exception as e:
        print(e)
    
    