import unittest
from find_lines import *
from point_set import *


class TestFindLines(unittest.TestCase):
    def test_three_points(self):
        test_points = [(1, 1), (2, 2), (3, 3)]
        ps = PointSet(test_points)
        valid_line_set = [(-1.0, 1.0, 0.0)]
        pt_threshold = num_points = 3
        self.assertAlmostEqual(find_unique_lines(ps, num_points, pt_threshold)[0], valid_line_set)
        self.assertAlmostEqual(find_max_unique_point_lines(ps, num_points, pt_threshold)[0], valid_line_set)

    def test_float_errors(self):
        test_points_float = [(1.0, 1.0), (2.0, 2.0), (3.0, 3.0)]  # Currently find_lines not tolerant to float values
        self.assertRaises(ValueError, find_unique_lines, True)
