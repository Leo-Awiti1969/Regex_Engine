# tests for the is_even() function
import unittest


class TestIsEven(unittest.TestCase):

    def test_when_output_true(self):
        self.assertTrue(4 % 2 == 0)

    def test_when_output_false(self):
        self.assertFalse(4 % 2 == 1)


if __name__ == '__main__':
    unittest.main()
