from unittest import TestCase
from p3_length_of_longest_substring import length_of_longest_substring


class Test(TestCase):
    def test_length_of_longest_substring(self):
        self.assertEqual(length_of_longest_substring("abcabcdd"), 4)
        self.assertEqual(length_of_longest_substring("dddddddd"), 1)
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)
        self.assertEqual(length_of_longest_substring(""), 0)
