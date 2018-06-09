import os
import sys
sys.path.append("./Tests")
import xmlrunner
import unittest
import MathFunctions

class TestMath(unittest.TestCase):
    def testAddOk(self):
        check = MathFunctions.Add(1, 2)
        self.assertEqual(check, 3)

    def testAddFail(self):
        check = MathFunctions.Add(1, 2)
        self.assertEqual(check, 4)

    def testAddMultipleOk(self):
        check = MathFunctions.AddMultipleArgs([1, 2, 3])
        self.assertEqual(check, 6)

    def testMultiplyOk(self):
        check = MathFunctions.Multiply(5, 4)
        self.assertEqual(check, 20)

    def testDivideOk(self):
        check = MathFunctions.Divide(20, 4)
        self.assertEqual(check, 5)

    def testSubtractOk(self):
        check = MathFunctions.Subtract(100, 15)
        self.assertEqual(check, 85)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))
