# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_038A import execute


class TestABC038A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('ICEDT'), 'YES')

    def test_execute_2(self):
        self.assertEqual(execute('MUGICHA'), 'NO')

    def test_execute_3(self):
        self.assertEqual(execute('OOLONGT'), 'YES')

    def test_execute_4(self):
        self.assertEqual(execute('T'), 'YES')
