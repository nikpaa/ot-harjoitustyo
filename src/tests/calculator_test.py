import unittest
import math
import parse
from operation import BinaryOperation, UnaryOperation
from errors import CalculatorError
from history import create_table, add_operation_to_db, clear_table


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
    def test_unsupported_binary_error(self):
        with self.assertRaises(CalculatorError):
            BinaryOperation("append")

    def test_str_method(self):
        operaatio = BinaryOperation("/")
        self.assertEqual(str(operaatio), "/")
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
    def test_log_error(self):
        operaatio = UnaryOperation("ln")
        with self.assertRaises(CalculatorError):
            operaatio.compute(-5)
    def test_unsupported_unary_error(self):
        with self.assertRaises(CalculatorError):
            UnaryOperation("permute")


class TestParsing(unittest.TestCase):
    def test_numberparsing(self):
        self.assertEqual(parse.parse_num("33.5 4 +"), (33.5, "4 +"))
    def test_inputparsing(self):
        self.assertEqual(parse.parse_input("5 exp 2 /"), (True, str(math.exp(5)/2)))

    def test_help(self):
        self.assertEqual(parse.parse_input("help"), (True, None))
    def test_operations(self):
        self.assertEqual(parse.parse_input("operations"), (True, None))
    def test_history(self):
        self.assertEqual(parse.parse_input("history"), (True, None))
    def test_exit(self):
        self.assertEqual(parse.parse_input("exit"), (False, None))

class TestDB(unittest.TestCase):
    # just test that these dont crash,
    # because the results are just printed, not returned
    def test_db(self):
        create_table()
        add_operation_to_db("1 1 +", "2")
        clear_table()
