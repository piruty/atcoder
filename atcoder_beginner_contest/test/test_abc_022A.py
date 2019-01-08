# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_022A import execute


class TestABC022A(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute(5, 60, 70, [50, 10, 10, 10, 10]), 2)

    def test_execute_2(self):
            self.assertEqual(execute(5, 50, 100, [120, -10, -20, -30, 70]), 2)
