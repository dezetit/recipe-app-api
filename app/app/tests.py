"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding two numbers"""
        result = calc.add(5, 6)
        self.assertEqual(result, 11)

    def test_subtract_numbers(self):
        result = calc.subtract(6, 5)
        self.assertEqual(result, 1)
