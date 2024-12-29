from unittest import TestCase
from main import solution, possible_win, count


class Test(TestCase):
    def test_solution(self):
        self.assertEqual(0, solution(["OOO", "XOX", "XXO"]))

    def test_possible_win(self):
        self.assertEqual(0, possible_win(["OOO", "OOO", "OOO"], "X"))

    def test_count(self):
        self.assertEqual(9, count(["OOO", "OOO", "OOO"], "O"))
