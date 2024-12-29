from unittest import TestCase
import p6_zigzag_conversion as p6


class Test(TestCase):
    def test_convert(self):
        expected = "PAHNAPLSIIGYIR"
        actual = p6.convert("PAYPALISHIRING", 3)
        self.assertEqual(expected, actual)

        expected = "PINALSIGYAHRPI"
        actual = p6.convert("PAYPALISHIRING", 4)
        self.assertEqual(expected, actual)

        expected = "ABDC"
        actual = p6.convert("ABCD", 3)
        self.assertEqual(expected, actual)
