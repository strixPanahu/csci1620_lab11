import area
from math import pi
from random import random
import unittest


class TestMethods(unittest.TestCase):

    def test_fail_circle_string(self):
        with self.assertRaises(ValueError):
            area.circle("X")

    def test_fail_square_string(self):
        with self.assertRaises(ValueError):
            area.square("X")

    def test_fail_rectangle_strings(self):
        with self.assertRaises(ValueError):
            area.rectangle("X", "X")

    def test_fail_rectangle_string_first(self):
        with self.assertRaises(ValueError):
            area.rectangle("X", 1)

    def test_fail_rectangle_string_second(self):
        with self.assertRaises(ValueError):
            area.rectangle(1, "X")

    def test_fail_triangle_strings(self):
        with self.assertRaises(ValueError):
            area.triangle("X", "X")

    def test_fail_triangle_string_first(self):
        with self.assertRaises(ValueError):
            area.triangle("X", 1)

    def test_fail_triangle_string_second(self):
        with self.assertRaises(ValueError):
            area.triangle(1, "X")

    def test_fail_circle_negative(self):
        with self.assertRaises(TypeError):
            area.circle(-2)

    def test_fail_square_negative(self):
        with self.assertRaises(TypeError):
            area.square(-2)

    def test_fail_rectangle_negatives(self):
        with self.assertRaises(TypeError):
            area.rectangle(-2, -2)

    def test_fail_rectangle_negative_first(self):
        with self.assertRaises(TypeError):
            area.rectangle(-2, 2)

    def test_fail_rectangle_negative_second(self):
        with self.assertRaises(TypeError):
            area.rectangle(2, -2)

    def test_fail_triangle_negatives(self):
        with self.assertRaises(TypeError):
            area.triangle(-2, -2)

    def test_fail_triangle_negative_first(self):
        with self.assertRaises(TypeError):
            area.triangle(-2, 2)

    def test_fail_triangle_negative_second(self):
        with self.assertRaises(TypeError):
            area.triangle(2, -2)

    def test_fail_circle_zero(self):
        with self.assertRaises(TypeError):
            area.circle(0)

    def test_fail_square_zero(self):
        with self.assertRaises(TypeError):
            area.square(0)

    def test_fail_rectangle_zeroes(self):
        with self.assertRaises(TypeError):
            area.rectangle(0, 0)

    def test_fail_rectangle_zero_first(self):
        with self.assertRaises(TypeError):
            area.rectangle(0, 2)

    def test_fail_rectangle_zero_second(self):
        with self.assertRaises(TypeError):
            area.rectangle(2, 0)

    def test_fail_triangle_zeroes(self):
        with self.assertRaises(TypeError):
            area.triangle(0, 0)

    def test_fail_triangle_zero_first(self):
        with self.assertRaises(TypeError):
            area.triangle(0, 2)

    def test_fail_triangle_zero_second(self):
        with self.assertRaises(TypeError):
            area.triangle(2, 0)

    def test_pass_circle_int(self):
        self.assertEqual(area.circle(int(2)), (2 ** 2) * pi)

    def test_pass_circle_float(self):
        self.assertEqual(area.circle(float(2)), (2 ** 2) * pi)

    def test_pass_square_int(self):
        self.assertEqual(area.square(int(2)), 4)

    def test_pass_square_float(self):
        self.assertEqual(area.square(float(2)), 4)

    def test_pass_rectangle_ints(self):
        self.assertEqual(area.rectangle(int(2), int(2)), 4)

    def test_pass_rectangle_floats(self):
        self.assertEqual(area.rectangle(float(2), float(2)), 4)

    def test_pass_rectangle_int_float(self):
        self.assertEqual(area.rectangle(int(2), float(2)), 4)

    def test_pass_rectangle_float_int(self):
        self.assertEqual(area.rectangle(float(2), int(2)), 4)

    def test_pass_triangle_ints(self):
        self.assertEqual(area.triangle(int(2), int(2)), 2)

    def test_pass_triangle_floats(self):
        self.assertEqual(area.triangle(float(2), float(2)), 2)

    def test_pass_triangle_int_float(self):
        self.assertEqual(area.triangle(int(2), float(2)), 2)

    def test_pass_triangle_float_int(self):
        self.assertEqual(area.triangle(float(2), int(2)), 2)

    def test_pass_circle_random(self):
        for i in range(10):
            param = random() * 100
            self.assertEqual(area.circle(param), (param ** 2) * pi)

    def test_pass_square_random(self):
        for i in range(10):
            param = random() * 100
            self.assertEqual(area.square(param), param * param)

    def test_pass_rectangle_random(self):
        for i in range(10):
            params = [random() * 100, random() * 100]
            self.assertEqual(area.rectangle(params[0], params[1]), params[0] * params[1])

    def test_pass_triangle_random(self):
        for i in range(10):
            params = [random() * 100, random() * 100]
            self.assertEqual(area.triangle(params[0], params[1]), (params[0] * params[1]) / 2)
