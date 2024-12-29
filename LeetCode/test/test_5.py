from unittest import TestCase
import p5_longest_palindrome as p5


class Test(TestCase):
    def test_longest_palindrome1(self):
        string = 'babad'
        expected = ['bab', 'aba']
        actual = p5.longest_palindrome(string)

        self.assertIn(actual, expected)

    def test_longest_palindrome2(self):
        string = 'cbbd'
        expected = ['bb']
        actual = p5.longest_palindrome(string)

        self.assertIn(actual, expected)

    def test_longest_palindrome3(self):
        string = 'bb'
        expected = ['bb']
        actual = p5.longest_palindrome(string)

        self.assertIn(actual, expected)
