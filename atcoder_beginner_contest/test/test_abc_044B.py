# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_044B import execute


class TestABC044B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute('abaccaba'), 'Yes')

    def test_execute_2(self):
        self.assertEqual(execute('hthth'), 'No')
