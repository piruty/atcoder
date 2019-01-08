# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_028B import execute


class TestABC028B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('BEAF'), '1 1 0 0 1 1')

    def test_execute_2(self):
        self.assertEqual(execute('DECADE'), '1 0 1 2 2 0')

    def test_execute_3(self):
        self.assertEqual(execute('ABBCCCDDDDEEEEEFFFFFF'), '1 2 3 4 5 6')
