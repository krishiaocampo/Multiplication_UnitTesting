import unittest


# n1 * n2
def mult(n1, n2):
        mult_of_numbers = n1 * n2
        return mult_of_numbers

class multTestCase(unittest.TestCase):
  
    def test_positive_numbers(self):
        result = mult(5, 10)
        self.assertEqual(result, 50)

    def test_negative_numbers(self):
        result = mult(-5, -10)
        self.assertEqual(result, 50)

    def test_zero(self):
        result = mult(0, 10)
        self.assertEqual(result, 0)

    def test_equal_numbers(self):
        result = mult(5, 5)
        self.assertEqual(result,25)

if __name__ == '__main__':
    unittest.main()