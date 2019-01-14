# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_046A import execute


class TestABC046A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(3, 1, 4), 3)

    def test_execute_2(self):
        self.assertEqual(execute(3, 3, 33), 2)
