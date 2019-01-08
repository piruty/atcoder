# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_043A import execute


class TestABC043A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(3), 6)

    def test_execute_2(self):
        self.assertEqual(execute(10), 55)

    def test_execute_3(self):
        self.assertEqual(execute(1), 1)
