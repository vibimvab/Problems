from unittest import TestCase
import p7_reverse_integer as p7


class Test(TestCase):
    def test_reverse(self):
        # self.assertEqual(0, p7.reverse(1534236469))
        self.assertEqual(0, p7.reverse(-1563847412))
