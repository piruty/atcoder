# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_013B import execute


class TestABC013B(TestCase):

    def test_execute_4_6(self):
            self.assertEqual(execute(4, 6), 2)

    def test_execute_6_4(self):
        self.assertEqual(execute(6, 4), 2)

    def test_execute_8_1(self):
        self.assertEqual(execute(8, 1), 3)
