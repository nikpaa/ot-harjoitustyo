import unittest
from operation import Operation

class TestOperation(unittest.TestCase):
    def setUp(self):
        self.operaatio = Operation("+")

    def test_compute(self):      
        self.assertEqual(self.operaatio.compute(1, 1), 2)