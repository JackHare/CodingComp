import unittest
import sys

sys.path.insert(1, "./Source/")

import demo as de

class TestDemo(unittest.TestCase):
    
    def test_sum_of_two_numbers(self):
        self.assertEqual(de.sum_of_two_nums(5,2), 7)
        
    def test_is_even(self):
        self.assertFalse(de.is_even(3))
        self.assertTrue(de.is_even(4))
        
if __name__ == '__main__':
    unittest.main()