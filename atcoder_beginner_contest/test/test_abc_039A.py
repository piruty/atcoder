# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_039A import execute


class TestABC039A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(2, 3, 4), 52)

    def test_execute_2(self):
        self.assertEqual(execute(3, 4, 2), 52)

    def test_execute_3(self):
        self.assertEqual(execute(100, 100, 100), 60000)

    def test_execute_4(self):
        self.assertEqual(execute(1, 1, 1), 6)
