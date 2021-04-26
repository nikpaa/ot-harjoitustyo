import unittest
from operation import Operation
import parse
from errors import CalculatorError

class TestOperation(unittest.TestCase):
    def test_plus(self):
        operaatio = Operation("+")
        self.assertEqual(operaatio.compute(1, 1), 2)

    def test_minus(self):
        operaatio = Operation("-")
        self.assertEqual(operaatio.compute(2, 1), 1)

    def test_mult(self):
        operaatio = Operation("*")
        self.assertEqual(operaatio.compute(40, 5), 200)

    def test_div(self):
        operaatio = Operation("/")
        self.assertEqual(operaatio.compute(10, 2), 5)

    def test_div_error(self):
        operaatio = Operation("/")
        with self.assertRaises(CalculatorError):
            operaatio.compute(7, 0)
    

class TestParsing(unittest.TestCase):
    def test_numberparsing(self):
        self.assertEqual(parse.parse_num("33.5 4 +"), (33.5, "4 +"))