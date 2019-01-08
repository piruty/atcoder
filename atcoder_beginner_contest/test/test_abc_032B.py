# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_032B import execute


class TestABC032B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('abcabc', 2), 3)

    def test_execute_2(self):
        self.assertEqual(execute('aaaaa', 1), 1)

    def test_execute_3(self):
        self.assertEqual(execute('hello', 10), 0)

    def test_execute_4(self):
        self.assertEqual(execute('aaaaa', 2), 1)
