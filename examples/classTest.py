import unittest
from io import StringIO
import sys

class TestClass:
    def __init__(self, item=None):
        self.list = []
        if item:
            self.list.append(item)

    def printItems(self):
        print(self.list)


class TestTestClass(unittest.TestCase):

    def test_init_with_item(self):
        test_item = 2
        test_class = TestClass(test_item)
        self.assertEqual(test_class.list, [test_item])

    def test_init_without_item(self):
        test_class = TestClass()
        self.assertEqual(test_class.list, [])

    def test_printItems(self):
        test_class = TestClass(3)
        capturedOutput = StringIO()          # Create StringIO object
        sys.stdout = capturedOutput          # Redirect stdout.
        test_class.printItems()              # Call the function.
        sys.stdout = sys.__stdout__          # Reset redirect.
        self.assertEqual(capturedOutput.getvalue().strip(), "[3]")

if __name__ == '__main__':
    unittest.main()