# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_034A import execute


class TestABC034A(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(12, 34), 'Better')

    def test_execute_2(self):
        self.assertEqual(execute(98, 56), 'Worse')
