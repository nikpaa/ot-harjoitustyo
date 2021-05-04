import unittest
from operation import BinaryOperation, UnaryOperation
import parse
from errors import CalculatorError
import math

class TestOperation(unittest.TestCase):
    def test_plus(self):
        operaatio = BinaryOperation("+")
        self.assertEqual(operaatio.compute(1, 1), 2)

    def test_minus(self):
        operaatio = BinaryOperation("-")
        self.assertEqual(operaatio.compute(2, 1), 1)

    def test_mult(self):
        operaatio = BinaryOperation("*")
        self.assertEqual(operaatio.compute(40, 5), 200)

    def test_div(self):
        operaatio = BinaryOperation("/")
        self.assertEqual(operaatio.compute(10, 2), 5)

    def test_div_error(self):
        operaatio = BinaryOperation("/")
        with self.assertRaises(CalculatorError):
            operaatio.compute(7, 0)
    def test_exp(self):
        operaatio = UnaryOperation("exp")
        self.assertEqual(operaatio.compute(2), math.exp(2))
    def test_log(self):
        operaatio = UnaryOperation("ln")
        self.assertEqual(operaatio.compute(5), math.log(5))

class TestParsing(unittest.TestCase):
    def test_numberparsing(self):
        self.assertEqual(parse.parse_num("33.5 4 +"), (33.5, "4 +"))
    def test_inputparsing(self):
        self.assertEqual(parse.parse_input("5 exp 2 /"), (True, str(math.exp(5)/2)))