# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_020B import execute


class TestABC020B(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute('1', '23'), '246')

    def test_execute_2(self):
            self.assertEqual(execute('999', '999'), '1999998')
