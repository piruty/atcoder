# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_014A import execute


class TestABC014A(TestCase):

    def test_execute_7_3(self):
        self.assertEqual(execute(7, 3), 2)

    def test_execute_5_5(self):
        self.assertEqual(execute(5, 5), 0)

    def test_execute_1_100(self):
        self.assertEqual(execute(1, 100), 99)

    def test_execute_25_12(self):
        self.assertEqual(execute(25, 12), 11)
