# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_032A import execute


class TestABC032A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(2, 3, 8), 12)

    def test_execute_2(self):
        self.assertEqual(execute(2, 2, 2), 2)

    def test_execute_3(self):
        self.assertEqual(execute(12, 8, 25), 48)
