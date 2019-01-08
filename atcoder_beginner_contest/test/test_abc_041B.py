# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_041B import execute


class TestABC041B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(2, 3, 4), 24)

    def test_execute_2(self):
        self.assertEqual(execute(10000, 1000, 100), 1000000000)

    def test_execute_3(self):
        self.assertEqual(execute(100000, 1, 100000), 999999937)

    def test_execute_4(self):
        self.assertEqual(execute(1000000000, 1000000000, 1000000000), 999999664)
