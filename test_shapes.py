import unittest
import shapes


class RectangleTest(unittest.TestCase):
    def test_area(self):
        rect = shapes.Rectangle(2, 4)
        expected = 8
        actual = rect.area()
        self.assertEqual(expected, actual)

    def test_perimeter(self):
        rect = shapes.Rectangle(2, 4)
        expected = 12
        actual = rect.perimeter()
        self.assertEqual(expected, actual)


class SquareTest(unittest.TestCase):
    def test_instantiation(self):
        self.assertTrue(issubclass(shapes.Square, shapes.Rectangle))


