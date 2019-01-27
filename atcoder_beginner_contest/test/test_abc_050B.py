# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_050B import execute


class TestABC050B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(3, [2, 1, 4], 2, [[1, 1], [2, 3]]), [6, 9])

    def test_execute_2(self):
        self.assertEqual(execute(5, [7, 2, 3, 8, 5], 3, [[4, 2], [1, 7], [4, 13]]), [19, 25, 30])
