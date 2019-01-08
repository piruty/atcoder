# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_017B import execute


class TestABC017B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('chokuou'), 'YES')

    def test_execute_2(self):
        self.assertEqual(execute('kuccho'), 'NO')

    def test_execute_1(self):
            self.assertEqual(execute('atcoder'), 'NO')
