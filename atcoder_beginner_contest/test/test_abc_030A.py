# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_030A import execute


class TestABC030A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(5, 2, 6, 3), 'AOKI')

    def test_execute_2(self):
        self.assertEqual(execute(100, 80, 100, 73), 'TAKAHASHI')

    def test_execute_3(self):
        self.assertEqual(execute(66, 30, 55, 25), 'DRAW')
