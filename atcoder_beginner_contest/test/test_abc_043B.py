# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_043B import execute


class TestABC043B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('01B0'), '00')

    def test_execute_2(self):
        self.assertEqual(execute('0BB1'), '1')
