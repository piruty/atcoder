# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_025A import execute


class TestABC025A(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute('abcde', 8), 'bc')

    def test_execute_2(self):
            self.assertEqual(execute('aeiou', 22), 'ue')

    def test_execute_3(self):
            self.assertEqual(execute('vwxyz', 25), 'zz')
