from is_subarray import is_subarray
import unittest 

class Test_TestIncrementDecrement(unittest.TestCase):

    def test_1(self):
        self.assertTrue(is_subarray([1, 2, 3, 4], [1, 2, 3]))

    def test_2(self):
        self.assertFalse(is_subarray([1, 2, 3, 4], [4,2]))

    def test_3(self):
        self.assertFalse(is_subarray([1,2,3,4,5], [1,3,5]))


        

if __name__ == '__main__':
    unittest.main()