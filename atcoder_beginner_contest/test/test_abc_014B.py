# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_014B import execute


class TestABC014B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(5, [1, 10, 100, 1000]), 101)

    def test_execute_2(self):
        self.assertEqual(execute(1048575, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 210)

    def test_execute_3(self):
        self.assertEqual(execute(0, [1000, 1000, 1000, 1000]), 0)


