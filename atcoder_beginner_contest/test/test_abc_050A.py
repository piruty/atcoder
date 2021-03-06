# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_050A import execute


class TestABC050A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('1', '+', '2'), 3)

    def test_execute_2(self):
        self.assertEqual(execute('5', '-', '7'), -2)
