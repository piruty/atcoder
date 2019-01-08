# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_021B import execute


class TestABC021B(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute(5, 1, 5, 3, [3, 4, 2]), 'YES')

    def test_execute_2(self):
            self.assertEqual(execute(7, 1, 3, 4, [2, 4, 2, 7]), 'NO')

    def test_execute_3(self):
            self.assertEqual(execute(4, 1, 4, 3, [2, 1, 3]), 'NO')

    def test_execute_4(self):
            self.assertEqual(execute(4, 1, 4, 3, [2, 4, 3]), 'NO')

    def test_execute_5(self):
            self.assertEqual(execute(20, 1, 4, 12, [2, 3, 5, 7, 8, 9, 10, 11, 12, 15, 13, 14]), 'YES')
