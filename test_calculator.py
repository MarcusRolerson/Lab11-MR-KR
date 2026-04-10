# https://github.com/MarcusRolerson/Lab11-MR-KR
# Partner 1: Kelly Rosa
# Partner 2: Marcus Rolerson
##https://github.com/MarcusRolerson/Lab11-MR-KR/tree/Test_calc/edits
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertequal(add(10, 5), 15)
        self.assertequal(add(-20, 5), 5)
        self.assertequal(add(3000, 1000), 4000)
    def test_subtract(self):
        self.assertequal(subtract(10, 5), 5)
        self.assertequal(subtract(-20, 5), -25)
        self.assertequal(subtract(3000, 1000), 2000)

    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 7), 0)


    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-2, 10), -5)
        self.assertAlmostEqual(div(4, 9), 2.25)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
      with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):

        self.assertEqual(logarithm(2, 8), 3.0)

        self.assertEqual(logarithm(10, 100), 2.0)

        self.assertEqual(logarithm(5, 125), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10, 0)

        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)

        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()