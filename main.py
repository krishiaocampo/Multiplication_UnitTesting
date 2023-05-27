import unittest


# n1 * n2
def mult(n1, n2):
        mult_of_numbers = n1 * n2
        return mult_of_numbers

class multTestCase(unittest.TestCase):
  
    def positive_numbersTest(self):
        result = mult(10, 20)
        self.assertEqual(result, 200)

    def negative_numbersTest(self):
        result = mult(-6, -6)
        self.assertEqual(result, 36)

    def zeronumbersTest(self):
        result = mult(0, 100)
        self.assertEqual(result, 0)

    def equal_numbersTest(self):
        result = mult(7, 7)
        self.assertEqual(result, 49)

if __name__ == '__main__':
    unittest.main()