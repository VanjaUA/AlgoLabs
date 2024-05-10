from rabin_karp import rabin_karp_search
import unittest 

class Test_rabin_karp(unittest.TestCase):

    def test_1(self):
        haystack = "Apple and Orange is Orange and Apple"
        needle = "Apple"
        result = rabin_karp_search(haystack, needle)
        expected_result = [0,31]

        self.assertEqual(result,expected_result)
    

if __name__ == '__main__':
    unittest.main()