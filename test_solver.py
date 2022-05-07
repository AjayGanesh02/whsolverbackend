import unittest
from solver import Solver

class TestSolverMethods(unittest.TestCase):

    def setUp(self):
        self.solver = Solver()
    
    def test_solve_empty(self):
        self.assertEqual(self.solver.solve(""), ["Invalid board string"])

    def test_solve_bad_char(self):
        self.assertEqual(self.solver.solve("a"), ["Invalid board string"])

    def test_solve_invalid_type(self):
        self.assertEqual(self.solver.solve(1), ["Invalid input type"])

    def test_solve_alphabet(self):
        self.assertTrue(len(self.solver.solve("abcdefghijklmnop")) > 0)

if __name__ == '__main__':
    unittest.main()