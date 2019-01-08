# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_016A import execute


class TestABC016A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(1, 1), 'YES')

    def test_execute_2(self):
        self.assertEqual(execute(2, 29), 'NO')

    def test_execute_3(self):
            self.assertEqual(execute(12, 6), 'YES')
