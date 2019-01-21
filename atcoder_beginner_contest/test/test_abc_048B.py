# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_048B import execute


class TestABC048B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(4, 8, 2), 3)

    def test_execute_2(self):
        self.assertEqual(execute(0, 5, 1), 6)

    def test_execute_3(self):
        self.assertEqual(execute(9, 9, 2), 0)

    def test_execute_4(self):
        self.assertEqual(execute(1, 1000000000000000000, 3), 333333333333333333)
