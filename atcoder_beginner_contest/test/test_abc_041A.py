# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_041A import execute


class TestABC041A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('atcoder', 3), 'c')

    def test_execute_2(self):
        self.assertEqual(execute('beginner', 1), 'b')

    def test_execute_3(self):
        self.assertEqual(execute('contest', 7), 't')

    def test_execute_4(self):
        self.assertEqual(execute('z', 1), 'z')
