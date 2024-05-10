from calculate_price import calculate_price
import unittest 

class Test_TestIncrementDecrement(unittest.TestCase):

    def test_1(self):
        self.assertEqual(calculate_price([50, 20, 30, 17, 100], 10),207)
    
    def test_2(self):
        self.assertEqual(calculate_price([1, 2, 3, 4, 5, 6, 7], 100),15)

    def test_3(self):
        self.assertEqual(calculate_price([1, 1, 1], 33),2.67)



        

if __name__ == '__main__':
    unittest.main()