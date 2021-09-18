import unittest

def product_function(first_arg, second_arg):
    result = first_arg * second_arg
    return result

class TestForFunction(unittest.TestCase):
    def test_product_function(self):
        self.assertTrue(product_function(2,3))   # check boolean(product_function(2,3)) == True?

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)