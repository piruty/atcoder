# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_031B import execute


class TestABC031B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(300, 400, 3, [240, 350, 480]), '60\n0\n-1')

    def test_execute_2(self):
        self.assertEqual(execute(50, 80, 5, [10000, 50, 81, 80, 0]), '-1\n0\n-1\n0\n50')
