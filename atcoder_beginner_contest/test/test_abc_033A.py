# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_033A import execute


class TestABC033A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('2222'), 'SAME')

    def test_execute_2(self):
        self.assertEqual(execute('1221'), 'DIFFERENT')

    def test_execute_3(self):
        self.assertEqual(execute('0000'), 'SAME')
