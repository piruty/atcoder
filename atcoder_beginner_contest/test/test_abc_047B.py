# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_047B import execute


class TestABC047B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(5, 4, 3, [[2, 1, 1], [3, 3, 4]]), 9)

    def test_execute_2(self):
        self.assertEqual(execute(5, 4, 3, [[2, 1, 1], [3, 3, 4], [1, 4, 2]]), 0)

    def test_execute_3(self):
        self.assertEqual(execute(10, 10, 5, [[1, 6, 1], [4, 1, 3], [6, 9, 4], [9, 4, 2], [3, 1, 3]]), 64)
