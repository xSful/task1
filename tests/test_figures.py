import unittest
from figure_area import figures

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = figures.Circle(10)
        self.assertEqual(circle.area(), 314.0)

    def test_triangle_area(self):
        triangle = figures.Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6.0)

    def test_right_triangle(self):
        triangle = figures.Triangle(3, 4, 5)
        self.assertTrue(triangle.is_rectangular())
    
    def test_rectangle_area(self):
        rectangle = figures.Rectangle(5, 5)
        self.assertEqual(rectangle.area(), 25.0)

if __name__ == "__main__":
    unittest.main()