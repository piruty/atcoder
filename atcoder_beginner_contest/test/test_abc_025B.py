# /usr/bin/env python
# coding: utf-8

from unittest import TestCase
from atcoder_beginner_contest.abc_025B import execute


class TestABC025B(TestCase):

    def test_execute_1(self):
        self.assertEqual(execute(3, 5, 10, [['East', 7], ['West', 3], ['West', 11]]), 'West 8')

    def test_execute_2(self):
        self.assertEqual(execute(3, 3, 8, [['West', 6], ['East', 3], ['East', 1]]), '0')

    def test_execute_3(self):
        self.assertEqual(execute(5, 25, 25, [['East', 1], ['East', 1], ['West', 1], ['East', 100], ['West', 1]]), 'East 25')
