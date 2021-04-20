import unittest
from operation import Operation
import parse

class TestOperation(unittest.TestCase):
    def setUp(self):
        self.operaatio = Operation("+")

    def test_compute(self):      
        self.assertEqual(self.operaatio.compute(1, 1), 2)

class TestParsing(unittest.TestCase):
    def test_numberparsing(self):
        self.assertEqual(parse.parse_num("33.5 4 +"), (33.5, "4 +"))