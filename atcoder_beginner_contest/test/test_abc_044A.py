# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_044A import execute


class TestABC044A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(5, 3, 10000, 9000), 48000)

    def test_execute_2(self):
        self.assertEqual(execute(2, 3, 10000, 9000), 20000)
