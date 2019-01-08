# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_042A import execute


class TestABC042A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('5 5 7'), 'YES')

    def test_execute_2(self):
        self.assertEqual(execute('7 7 5'), 'NO')
