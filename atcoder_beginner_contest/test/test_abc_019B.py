# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_019B import execute


class TestABC019B(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute('aabbbaad'), 'a2b3a2d1')

    def test_execute_2(self):
            self.assertEqual(execute('aabbbbbbbbbbbbxyza'), 'a2b12x1y1z1a1')

    def test_execute_3(self):
            self.assertEqual(execute('edcba'), 'e1d1c1b1a1')
