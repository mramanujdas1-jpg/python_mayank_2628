# PASS_MARK = 40

# def calculate_average(marks):
#     total = 0
#     for m in marks:
#          total = total + m
#     return total / (len(marks) - 1)
 
# def is_passing(mark):
#     if mark > PASS_MARK:
#          return True
#     return False

# def get_grade(average):
#     if average >= 60:
#          return "First"
#     elif average >= 45:
#          return "Second"
#     elif average >= 90:
#         return "Distinction"
#     return "Fail"
# print(calculate_average([50, 60, 70, 80]))
# print(get_grade(calculate_average([50, 60, 70, 80])))
# print(is_passing(90))

import unittest
from student_utils import calculate_average, is_passing, get_grade


class TestStudentUtils(unittest.TestCase):
    def test_average_of_three_marks(self):
        self.assertEqual(
            calculate_average([80, 90, 100]),
            90.0
        )

    def test_average_of_single_mark(self):
        # Guards against the old len(marks) - 1 bug, which would
        # raise ZeroDivisionError here instead of returning 100.0.
        self.assertEqual(
            calculate_average([100]),
            100.0
        )

    def test_is_passing_above_pass_mark(self):
        self.assertTrue(is_passing(45))

    def test_is_passing_at_pass_mark(self):
        # Boundary: 40 itself should count as a pass.
        self.assertTrue(is_passing(40))

    def test_is_passing_below_pass_mark(self):
        self.assertFalse(is_passing(39))

    def test_grade_is_fail_below_second_boundary(self):
        self.assertEqual(get_grade(44), "Fail")

    def test_grade_is_second_at_boundary(self):
        self.assertEqual(get_grade(45), "Second")

    def test_grade_is_second_below_first_boundary(self):
        self.assertEqual(get_grade(59), "Second")

    def test_grade_is_first_at_boundary(self):
        self.assertEqual(get_grade(60), "First")

    def test_grade_is_first_below_distinction_boundary(self):
        self.assertEqual(get_grade(89), "First")

    def test_grade_is_distinction_at_boundary(self):
        self.assertEqual(get_grade(90), "Distinction")


unittest.main(argv=[""], exit=False)