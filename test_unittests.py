from bfs import read_input_file,bfs
import unittest 

class Test_bfs(unittest.TestCase):

    def test_1(self):
        start_point, end_point, matrix = read_input_file('input.txt')
        min_distance = bfs(matrix, *start_point, *end_point)
        expected_distance = 12
        self.assertEqual(min_distance,expected_distance)
    

if __name__ == '__main__':
    unittest.main()