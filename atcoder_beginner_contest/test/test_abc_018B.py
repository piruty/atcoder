# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_018B import execute


class TestABC018B(TestCase):

    def test_execute_1(self):
            self.assertEqual(execute('abcdef', [[3, 5], [1, 4]]), 'debacf')

    def test_execute_2(self):
        self.assertEqual(execute('redcoat', [[1, 7], [1, 2], [3, 4]]), 'atcoder')
