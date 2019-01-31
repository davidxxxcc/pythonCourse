import unittest
import UnitTest_unittest as ut

# https://docs.python.org/2/library/unittest.html#assert-methods
class TestClac(unittest.TestCase):

    def test_add(self):
        self.assertEquals(ut.add(10, 5) , 15)
        self.assertEquals(ut.add(-1, -1), -2)
        self.assertEquals(ut.add(-5, 5), 0)

    def test_subtract(self):
        self.assertEquals(ut.subtract(10, 5) , 5)
        self.assertEquals(ut.subtract(-1, -1), 0)
        self.assertEquals(ut.subtract(-5, 5), -10)

    def test_multiply(self):
        self.assertEquals(ut.multiply(10, 5) , 50)
        self.assertEquals(ut.multiply(-1, -1), 1)
        self.assertEquals(ut.multiply(-5, 5), -25)

    def test_divide(self):
        self.assertEquals(ut.divide(10, 5) , 2)
        self.assertEquals(ut.divide(-1, -1), 1)
        self.assertEquals(ut.divide(-5, 5), -1)

        self.assertRaises(ValueError, ut.divide, 10, 0)


if __name__ == '__main__':
    unittest.main()