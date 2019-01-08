# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_023B import execute


class TestABC023B(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute(3, 'abc'), 1)

    def test_execute_2(self):
            self.assertEqual(execute(6, 'abcabc'), -1)

    def test_execute_3(self):
            self.assertEqual(execute(7, 'atcoder'), -1)

    def test_execute_4(self):
            self.assertEqual(execute(19, 'bcabcabcabcabcabcab'), 9)
