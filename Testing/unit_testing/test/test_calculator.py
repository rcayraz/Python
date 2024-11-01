import unittest
from src.calculator import sum


class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()

