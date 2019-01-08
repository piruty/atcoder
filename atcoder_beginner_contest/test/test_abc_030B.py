# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_030B import execute


class TestABC030B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(15, 0), 90)

    def test_execute_2(self):
        self.assertEqual(execute(3, 17), 3.5)

    def test_execute_3(self):
        self.assertEqual(execute(0, 0), 0)

    def test_execute_4(self):
        self.assertEqual(execute(6, 0), 180)

    def test_execute_5(self):
        self.assertEqual(execute(23, 59), 5.5000)

    def test_execute_6(self):
        self.assertEqual(execute(1, 59), 1)
