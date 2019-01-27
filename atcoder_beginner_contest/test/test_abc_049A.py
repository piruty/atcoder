# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_049A import execute


class TestABC049A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('a'), 'vowel')

    def test_execute_2(self):
        self.assertEqual(execute('z'), 'consonant')

    def test_execute_3(self):
        self.assertEqual(execute('s'), 'consonant')
