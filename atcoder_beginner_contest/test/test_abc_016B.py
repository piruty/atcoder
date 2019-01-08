# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_016B import execute


class TestABC016B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(1, 0, 1), '?')

    def test_execute_2(self):
        self.assertEqual(execute(1, 1, 2), '+')

    def test_execute_3(self):
        self.assertEqual(execute(1, 1, 0), '-')

    def test_execute_4(self):
        self.assertEqual(execute(1, 1, 1), '!')
