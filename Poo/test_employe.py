import unittest
from employe import Employee

class TestEmployee(unittest.TestCase):
    def test_init(self):
        employee = Employee("Alice", 2000)
        self.assertEqual(employee.name, "Alice")
        self.assertEqual(employee.salary, 2000)

if __name__ == '__main__':
    unittest.main()