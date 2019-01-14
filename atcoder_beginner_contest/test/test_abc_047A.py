# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_047A import execute


class TestABC047A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(10, 30, 20), 'Yes')

    def test_execute_2(self):
        self.assertEqual(execute(30, 30, 100), 'No')

    def test_execute_3(self):
        self.assertEqual(execute(56, 25 ,31), 'Yes')
