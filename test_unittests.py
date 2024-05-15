import unittest
import os
from govern import topological_sort, read_input

class Test_Govern(unittest.TestCase):
    def test1(self):
        input_file_path = os.path.abspath('test1.in')

        result = topological_sort(read_input(input_file_path))
        expected_result = ['birthcertificate', 'nationalpassport', 'militarycertificate', 'foreignpassport', 'creditcard', 'hotel', 'bankstatement', 'visa']
        self.assertEqual(result,expected_result)

    def test2(self):
        input_file_path = os.path.abspath('test2.in')

        result = topological_sort(read_input(input_file_path))
        expected_result = ['foreignpassport', 'visa']
        self.assertEqual(result,expected_result)    

if __name__ == "__main__":
    unittest.main()
